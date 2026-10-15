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

print("After 'i':",pair_counts["i"])     
print("After 'love':",pair_counts["love"])  
print("After 'ai':",pair_counts["ai"]) 

pair_prods = {}

for current_word in pair_counts:
    pair_prods[current_word]={}
    total=sum(pair_counts[current_word].values())

    for next_word in pair_counts[current_word]:
        pair_prods[current_word][next_word]=pair_counts[current_word][next_word]/total

print ("\n probality after 'i':")        