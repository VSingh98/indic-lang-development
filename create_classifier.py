import nltk
from nltk import *
import random
from open_files import open_x_features


def orderLanguageCodes(lang_codes):

    if 'h' in lang_codes:
        lang_codes = 'h'+lang_codes.replace('h','')

    if 's' in lang_codes:
        lang_codes = 's'+lang_codes.replace('s','')

    if 'p' in lang_codes:
        lang_codes = 'p'+lang_codes.replace('p','')

    if 'm' in lang_codes:
        lang_codes = 'm'+lang_codes.replace('m','')

    #print lang_codes

    return lang_codes

'''
@Name: create_classifier

@Desc:  Given a string of language codes, it creates a corresponding
        NaiveBayesClassifier. By default, test size is twenty percent of our
        overall data

@Param: lang_codes:     These are the languages we are creating a clsfir for 
        training_size:  how many words we want for each language
        test_size:      how many we want for each test size

@Return: (<classifier>, <classifier accuracy on 20% of data>)


def create_NaiveBayesClassifier(lang_codes, training_size, flag=True, n=2):

    corpora_dict = {'h': 'hindi', 'm': 'marathi', 'p': 'pali', 's':'sanskrit'}

    lang_codes = orderLanguageCodes(lang_codes)
    
    feature_list = list()

    training_min = False

    for lang in lang_codes:
        
        training_set = open_x_features(training_size, lang, flag, n)
        
        if training_min is False: 
            training_size = len(training_set)
            training_min = True     
       
        feature_list += [(feature, corpora_dict[lang] ) for feature in training_set]
        
    
    random.shuffle(feature_list)

    feature_set= [({'feature':n},language)for (n,language)in feature_list]

    # we will create a test set of 20%
    test_size = int(len(feature_set)*.2)

    test_set = feature_set[:test_size]
    training_set = feature_set[test_size:]

    #print "about to start training"

    #ok now we are training the classifier. Hooray!
    classifier = nltk.NaiveBayesClassifier.train(training_set)

    #print "finished training"

    return(classifier, (nltk.classify.accuracy(classifier,test_set)), training_size )
'''

def create_NaiveBayesClassifier(test_set, training_set):

    #ok now we are training the classifier. Hooray!
    classifier = nltk.NaiveBayesClassifier.train(training_set)

    #print "finished training"

    return(classifier, (nltk.classify.accuracy(classifier,test_set)))

    