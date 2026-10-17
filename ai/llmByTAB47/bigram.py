text = """"
I love AI
I love coding
I love Python
I like AI
I like coding
I enjoy Python
"""

words = text.lower().split()

pair_counts = {}

for i in range(len(words)-1):
    current_word=words[i]
    next_word=words[i+1]

    if current_word not in pair_counts:
        pair_counts[current_word]={}

    if next_word not in pair_counts[current_word]:
        pair_counts[current_word][next_word]=0    

    pair_counts[current_word][next_word]+=1   

# print("After 'i':",pair_counts["i"])     
# print("After 'love':",pair_counts["love"])  
# print("After 'ai':",pair_counts["ai"]) 

pair_prods = {}

for current_word in pair_counts:
    pair_prods[current_word]={}
    total=sum(pair_counts[current_word].values())

    for next_word in pair_counts[current_word]:
        pair_prods[current_word][next_word]=pair_counts[current_word][next_word]/total

# print ("\n probality after 'like':")  
# for word,prob in sorted(pair_prods["like"].items(),key = lambda x: -x[1]):
#     print(f"{word} : {prob:.1%}")  


#----------------
import random

def generate_token(start_word , num_word = 5):
    current_word = start_word
    output = [current_word]

    for _ in range(num_word):
        # dead end -> this not folled by anything
        if current_word not in pair_prods:
            break

        # get the options and their probads
        options = list(pair_prods[current_word].keys())
        probabilities = list(pair_prods[current_word].values())

        # sample the responses from the distribution
        next_word = random.choices(options , weights = probabilities , k=1)[0]

        output.append(next_word)
        current_word = next_word
    return " ".join(output)   

print("text genrated by bigram model")
for i in range(5):
    print(f"{i+1}.{generate_token('i')}") 