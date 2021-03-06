import nltk
from nltk import *
from re import *
import random
from ngram_splitter import ngram
from io import open
#opening the hindi text and putting its words in a list
f = open("C:/Users/Sam/Documents/School/Lign 165/projectnext/project/hindi/90_utf.txt.norm",encoding="utf-8" )
hindi_corpus = f.read()
tokenized_hindi_corpus = hindi_corpus.split()
hindi_bigrams = []
for word in tokenized_hindi_corpus:
    hindi_bigrams += ngram(word,2)
tupled_hindi_words = ([(word, 'hindi') for word in hindi_bigrams])
f.close()
#opening the marathi text and putting its words in a list
g = open("C:/Users/Sam/Documents/School/Lign 165/projectnext/project/marathi/astro1.txt.norm", encoding="utf-8")
marathi_corpus = g.read()
tokenized_marathi_corpus = marathi_corpus.split()
marathi_bigrams = []
for word in tokenized_marathi_corpus:
    marathi_bigrams += ngram(word,2)
tupled_marathi_words= ([(word, 'marathi') for word in marathi_bigrams])
g.close()

#combining to one big set for testing and development.
the_set = tupled_marathi_words + tupled_hindi_words
random.shuffle(the_set)
#print (the_set)
#print (len(the_set))
featureset= [({'bigram':n},language)for (n,language)in the_set]
train_set = featureset[:6000]
test_set = featureset[6000:]
print (featureset)
#ok now we are training the classifier. Hooray!
classifier = nltk.NaiveBayesClassifier.train(train_set)
#print (classifier.classify({'word':''}))
#now we are testing it on the test set
print(nltk.classify.accuracy(classifier,test_set))
