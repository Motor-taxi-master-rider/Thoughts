from nltk import ngrams
from nltk.book import *

fourgrams = ngrams(text6, 4)
for fourgram in fourgrams: 
    if fourgram[0] == "coconut": 
        print(fourgram)
