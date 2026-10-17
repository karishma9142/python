text = """
I love AI
I love coding
I love Python
I like AI
I like coding
I enjoy Python
"""

words = text.lower().split()

def build_ngram_model(words , n=2):
    counts = {}

    for i in range(len(words)-n+1):
        context = tuple(words[i: i+n-1])
        target = words[i+n-1]

        if context not in counts:
            counts[context] = {}

        if target not in counts[context]:
            counts[context][target] = 0

        counts[context][target] +=1    

    probs = {}
    for context in counts:
        total = sum(counts[context].values())
        probs[context]={}

        for target in counts[context]:
            probs[context][target] = counts[context][target]/total

    return probs            

bigram = build_ngram_model(words,2)
trigram =build_ngram_model(words,3)
fourgram = build_ngram_model(words,4)

print("baigram after love :")
for w ,p in sorted (bigram[("love",)].items(),key = lambda x: -x[1])[:5]:
    print(f" {w} : {p: .1%}")

print("trigram after i , love :")
if("i" , "love") in trigram:
    for w ,p in sorted (trigram[("i","love",)].items() ,key = lambda x: -x[1])[:5]:
        print(f" {w} : {p: .1%}")    


import random
def generate_ngram(model,n,start_words,num_words):
    output = list(start_words)      