import nltk
from nltk import *
from re import *
import random
from ngram_splitter import ngram
#opening the hindi text and putting its words in a list
f = open("C:/Users/Sam/Documents/School/Lign 165/projectnext/project/hindi/90_utf.txt.norm",encoding="utf8" )
the_text = f.read()
words = the_text.split()
bigrams = []
for word in words:
    bigrams += ngram(word,2)
hindi_words = ([(word, 'hindi') for word in bigrams])
f.close()
#opening the marathi text and putting its words in a list
g = open("C:/Users/Sam/Documents/School/Lign 165/projectnext/project/marathi/astro1.txt.norm",encoding="utf8")
marathi_text = g.read()
other_words = marathi_text.split()
other_bigrams = []
for word in other_words:
    other_bigrams += ngram(word,2)
marathi_words= ([(word, 'marathi') for word in other_bigrams])
g.close()

#combining to one big set for testing and development.
the_set = marathi_words + hindi_words
random.shuffle(the_set)
#print (the_set)
#print (len(the_set))
featureset= [({'bigram':n},language)for (n,language)in the_set]
train_set = featureset[:6000]
test_set = featureset[6000:]
print (featureset)
#ok now we are training the classifier. Hooray!
classifier = nltk.NaiveBayesClassifier.train(train_set)
#print (classifier.classify({'word':'सब'}))
#now we are testing it on the test set
print(nltk.classify.accuracy(classifier,test_set))
