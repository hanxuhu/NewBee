import re, collections
<<<<<<< HEAD
from nltk.stem.porter import PorterStemmer
#import createindex.Preprocess as Preprocess
=======
 
>>>>>>> upstream/master
def words(text): return re.findall('[a-z]+', text.lower()) 
 
def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model
 
<<<<<<< HEAD
#NWORDS = train(words(open('text.txt').read()))
=======
NWORDS = train(words(open('text.txt',encoding='utf-8').read()))
>>>>>>> upstream/master
 
alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)
 
def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)
 
def known(words): return set(w for w in words if w in NWORDS)
 
def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

<<<<<<< HEAD

#texts = open('big.txt').read()
def spellchecker(words):
    wordlist = Preprocess(words)
    wordlist_= []
    for word in wordlist:
        word_ = correct(word)
        wordlist_.append(word_)
    res = ""
    for word in wordlist_:
        res+=word+" "
    return res

import pickle

def Preprocess(query):
    stemmer_porter = PorterStemmer()

    query = query.lower()
    query = query.replace('-',' ')
    query = query.split(' ')
    stemmed_query = []
    for word in query:
        stemmed_query.append(stemmer_porter.stem(word))
    return stemmed_query


with open('NWORDS.pkl', 'rb') as f:
    NWORDS = pickle.load(f)
word =spellchecker("the dark nigt")
print(word)
=======
word =correct("nigt")
print(word)
#texts = open('big.txt').read()
#print(texts[:1000])

>>>>>>> upstream/master
