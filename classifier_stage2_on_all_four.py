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
#opening sanskrit text and putting words in a list
h = open("C:/Users/Sam/Documents/School/Lign 165/projectnext/project/sanskrit/mbs01001dev.txt.norm", encoding="utf-8")
sanskrit_corpus = h.read()
tokenized_sanskrit_corpus = sanskrit_corpus.split()
sanskrit_bigrams = []
for word in tokenized_sanskrit_corpus:
    sanskrit_bigrams += ngram(word,2)
tupled_sanskrit_words= ([(word, 'sanskrit') for word in sanskrit_bigrams])
h.close()
# opening a pali file and doing all those

i = open("C:/Users/Sam/Documents/School/Lign 165/projectnext/project/pali/vinaayapitak_1.txt.norm", encoding="utf-8")
pali_corpus = i.read()
tokenized_sanskrit_corpus = pali_corpus.split()
pali_bigrams = []
for word in tokenized_sanskrit_corpus:
    pali_bigrams += ngram(word,2)
tupled_pali_words= ([(word, 'pali') for word in pali_bigrams])
i.close()

'''
OK, NOW WE ARE COMPOSING A TEST SET AND A DEVELOPMENT SET FOR MARATHI AND HINDI. 
WE ARE THEN HAVING IT TRAIN AND PRINT ITS ACCURACY
'''
#combining to one big set for testing and development.
marathi_hindi_set = tupled_marathi_words + tupled_hindi_words
random.shuffle(marathi_hindi_set)
#print (the_set)
#print (len(the_set))
marathi_hindi_featureset= [({'bigram':n},language)for (n,language)in marathi_hindi_set]
marathi_hindi_train_set = marathi_hindi_featureset[:6000]
marathi_hindi_test_set = marathi_hindi_featureset[6000:]
#ok now we are training the classifier. Hooray!
marathi_hindi_classifier = nltk.NaiveBayesClassifier.train(marathi_hindi_train_set)
#print (classifier.classify({'word':''}))
#now we are testing it on the test set
print("marathi hindi accuracy: " + str(nltk.classify.accuracy(marathi_hindi_classifier,marathi_hindi_test_set)))

'''
OK, NOW WE ARE COMPOSING A TEST SET AND A DEVELOPMENT SET FOR HINDI AND PALI. 
WE ARE THEN HAVING IT TRAIN AND PRINT ITS ACCURACY
'''
#combining to one big set for testing and development.
hindi_pali_set = tupled_hindi_words + tupled_pali_words
random.shuffle(hindi_pali_set)
#print (the_set)
#print (len(the_set))
hindi_pali_featureset= [({'bigram':n},language)for (n,language)in hindi_pali_set]
hindi_pali_train_set = hindi_pali_featureset[:6000]
hindi_pali_test_set = hindi_pali_featureset[6000:]
#ok now we are training the classifier. Hooray!
hindi_pali_classifier = nltk.NaiveBayesClassifier.train(hindi_pali_train_set)
#print (classifier.classify({'word':''}))
#now we are testing it on the test set
print("hindi pali accuracy: " + str(nltk.classify.accuracy(hindi_pali_classifier,hindi_pali_test_set)))

'''
OK, NOW WE ARE COMPOSING A TEST SET AND A DEVELOPMENT SET FOR HINDI AND SANSKRIT. 
WE ARE THEN HAVING IT TRAIN AND PRINT ITS ACCURACY
'''
#combining to one big set for testing and development.
hindi_sanskrit_set = tupled_hindi_words + tupled_sanskrit_words
random.shuffle(hindi_sanskrit_set)
#print (the_set)
#print (len(the_set))
hindi_sanskrit_featureset= [({'bigram':n},language)for (n,language)in hindi_sanskrit_set]
hindi_sanskrit_train_set = hindi_sanskrit_featureset[:6000]
hindi_sanskrit_test_set = hindi_sanskrit_featureset[6000:]
#ok now we are training the classifier. Hooray!
hindi_sanskrit_classifier = nltk.NaiveBayesClassifier.train(hindi_sanskrit_train_set)
#print (classifier.classify({'word':''}))
#now we are testing it on the test set
print("hindi sanskrit accuracy: " + str(nltk.classify.accuracy(hindi_sanskrit_classifier,hindi_sanskrit_test_set)))

'''
OK, NOW WE ARE COMPOSING A TEST SET AND A DEVELOPMENT SET FOR MARATHI AND PALI. 
WE ARE THEN HAVING IT TRAIN AND PRINT ITS ACCURACY
'''
#combining to one big set for testing and development.
marathi_pali_set = tupled_marathi_words + tupled_pali_words
random.shuffle(marathi_pali_set)
#print (the_set)
#print (len(the_set))
marathi_pali_featureset= [({'bigram':n},language)for (n,language)in marathi_pali_set]
marathi_pali_train_set = marathi_pali_featureset[:6000]
marathi_pali_test_set = marathi_pali_featureset[6000:]
#ok now we are training the classifier. Hooray!
marathi_pali_classifier = nltk.NaiveBayesClassifier.train(marathi_pali_train_set)
#print (classifier.classify({'word':''}))
#now we are testing it on the test set
print("marathi pali accuracy: " + str(nltk.classify.accuracy(marathi_pali_classifier,marathi_pali_test_set)))

'''
OK, NOW WE ARE COMPOSING A TEST SET AND A DEVELOPMENT SET FOR MARATHI AND SANSKRIT. 
WE ARE THEN HAVING IT TRAIN AND PRINT ITS ACCURACY
'''
#combining to one big set for testing and development.
marathi_sanskrit_set = tupled_marathi_words + tupled_sanskrit_words
random.shuffle(marathi_sanskrit_set)
#print (the_set)
#print (len(the_set))
marathi_sanskrit_featureset= [({'bigram':n},language)for (n,language)in marathi_sanskrit_set]
marathi_sanskrit_train_set = marathi_sanskrit_featureset[:6000]
marathi_sanskrit_test_set = marathi_sanskrit_featureset[6000:]
#ok now we are training the classifier. Hooray!
marathi_sanskrit_classifier = nltk.NaiveBayesClassifier.train(marathi_sanskrit_train_set)
#print (classifier.classify({'word':''}))
#now we are testing it on the test set
print("Marathi Sanskrit accuracy: " + str(nltk.classify.accuracy(marathi_sanskrit_classifier,marathi_sanskrit_test_set)))
marathi_hindi_classifier.show_most_informative_features(5)