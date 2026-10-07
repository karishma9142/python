import os
import ast
import json
import operator

from dotenv import load_dotenv
from groq import Groq
from tavily import TavilyClient

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
load_dotenv()

my_api_key = os.getenv('GROQ_API_KEY')
if not my_api_key:
    raise ValueError('api key is missing')

tavily_api_key = os.getenv('TAVILY_API_KEY')
if not tavily_api_key:
    raise ValueError('tavily api key is missing')

client = Groq(api_key=my_api_key)
tavily_client = TavilyClient(api_key=tavily_api_key)
groqModel = 'openai/gpt-oss-120b'


# ---------------------------------------------------------------------------
# Tool 1: web search (Tavily)
# ---------------------------------------------------------------------------
def web_search(query: str) -> str:
    """Search the web with Tavily and return an answer plus top sources."""
    try:
        response = tavily_client.search(
            query=query,
            search_depth='basic',
            max_results=5,
            include_answer=True,
        )
    except Exception as e:
        return f'Web search failed: {e}'

    answer = response.get('answer') or 'No direct answer found.'
    sources = []
    for r in response.get('results', []):
        sources.append(f"- {r.get('title', '')} ({r.get('url', '')}): {r.get('content', '')[:300]}")

    return f'Answer: {answer}\n\nSources:\n' + '\n'.join(sources)


# ---------------------------------------------------------------------------
# Tool 2: calculator (safe evaluation, no eval())
# ---------------------------------------------------------------------------
_BIN_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}
_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _eval_node(node):
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.BinOp) and type(node.op) in _BIN_OPS:
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        if isinstance(node.op, ast.Pow) and abs(right) > 1000:
            raise ValueError('Exponent too large')
        return _BIN_OPS[type(node.op)](left, right)
    if isinstance(node, ast.UnaryOp) and type(node.op) in _UNARY_OPS:
        return _UNARY_OPS[type(node.op)](_eval_node(node.operand))
    raise ValueError('Unsupported expression')


def calculate(expression: str) -> str:
    """Evaluate a basic math expression like '2*2' and return the result."""
    try:
        tree = ast.parse(expression.strip(), mode='eval')
        result = _eval_node(tree)
        return str(result)
    except ZeroDivisionError:
        return 'Error: division by zero'
    except Exception as e:
        return f'Error: could not evaluate expression ({e})'


# ---------------------------------------------------------------------------
# Tools object (standard OpenAI-style function tool schema)
# ---------------------------------------------------------------------------
tools = [
    {
        'type': 'function',
        'function': {
            'name': 'web_search',
            'description': (
                'Search the web for current or factual information such as news, '
                'people, events, prices, or anything that needs up-to-date data. '
                'Takes a search query and returns an answer with sources.'
            ),
            'parameters': {
                'type': 'object',
                'properties': {
                    'query': {
                        'type': 'string',
                        'description': 'The search query to look up on the web.',
                    }
                },
                'required': ['query'],
            },
        },
    },
    {
        'type': 'function',
        'function': {
            'name': 'calculate',
            'description': (
                'Evaluate a basic arithmetic expression using + - * / // % ** and '
                'parentheses. Example: "2*2" or "(10+5)/3".'
            ),
            'parameters': {
                'type': 'object',
                'properties': {
                    'expression': {
                        'type': 'string',
                        'description': 'The math expression to evaluate, e.g. "2*2".',
                    }
                },
                'required': ['expression'],
            },
        },
    },
]

# Map tool names to the actual python functions
available_functions = {
    'web_search': web_search,
    'calculate': calculate,
}


# ---------------------------------------------------------------------------
# Agent loop
# ---------------------------------------------------------------------------
def run_agent(user_input: str, max_steps: int = 5) -> str:
    messages = [
        {
            'role': 'system',
            'content': (
                'You are a helpful assistant with two tools: web_search for '
                'real-world/current information and calculate for math. '
                'Use a tool only when needed, then give a clear final answer.'
            ),
        },
        {'role': 'user', 'content': user_input},
    ]

    for _ in range(max_steps):
        response = client.chat.completions.create(
            model=groqModel,
            messages=messages,
            tools=tools,
            tool_choice='auto',
        )
        msg = response.choices[0].message

        # No tool call -> this is the final answer
        if not msg.tool_calls:
            return msg.content

        # Record the assistant's tool call request
        messages.append({
            'role': 'assistant',
            'content': msg.content or '',
            'tool_calls': [
                {
                    'id': tc.id,
                    'type': 'function',
                    'function': {
                        'name': tc.function.name,
                        'arguments': tc.function.arguments,
                    },
                }
                for tc in msg.tool_calls
            ],
        })

        # Execute each requested tool and send back the result
        for tc in msg.tool_calls:
            name = tc.function.name
            try:
                args = json.loads(tc.function.arguments or '{}')
            except json.JSONDecodeError:
                args = {}

            func = available_functions.get(name)
            if func is None:
                result = f'Error: unknown tool {name}'
            else:
                try:
                    result = func(**args)
                except TypeError as e:
                    result = f'Error: bad arguments ({e})'

            print(f'[tool called] {name}({args}) -> {str(result)[:150]}')

            messages.append({
                'role': 'tool',
                'tool_call_id': tc.id,
                'name': name,
                'content': str(result),
            })

    return 'Sorry, I could not finish within the allowed number of steps.'


if __name__ == '__main__':
    user_query = input('Ask anything: ')
    print('\nAnswer:', run_agent(user_query))