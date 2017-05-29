import nltk
from nltk import *
import random
from open_files import open_x_words


'''
@Name: create_classifier

@Desc:  Given a string of language codes, it creates a corresponding
        NaiveBayesClassifier. By default, test size is twenty percent of our
        overall data

@Param: lang_codes:     These are the languages we are creating a clsfir for 
        training_size:  how many words we want for each language
        test_size:      how many we want for each test size

@Return: (<classifier>, <classifier accuracy on 20% of data>)
'''
def create_NaiveBayesClassifier(lang_codes, training_size):

    corpora_dict = {'h': 'hindi', 'm': 'marathi', 'p': 'pali', 's':'sanskrit'}

    if 'h' in lang_codes:
        lang_codes = 'h'+lang_codes.replace('h','')

    if 's' in lang_codes:
        lang_codes = 's'+lang_codes.replace('s','')

    if 'p' in lang_codes:
        lang_codes = 'p'+lang_codes.replace('p','')

    if 'm' in lang_codes:
        lang_codes = 'm'+lang_codes.replace('m','')
    
    word_feature_list = list()

    training_min = None

    for lang in lang_codes:
        
        if training_min is None:       
            training_min = open_x_words(training_size, lang)
            training_set = training_min
        
        else:
            training_set = open_x_words(training_min, lang)

      
        word_feature_list += [(word, corpora_dict[lang] ) for word in training_set]
        
    
    random.shuffle(word_feature_list)

    feature_set= [({'word':n},language)for (n,language)in word_feature_list]

    # we will create a test set of 20%
    test_size = int(len(feature_set)*.2)

    test_set = feature_set[:test_size]
    training_set = feature_set[test_size:]

    print "about to start training"

    #ok now we are training the classifier. Hooray!
    classifier = nltk.NaiveBayesClassifier.train(training_set)

    print "finished training"

    return(classifier, (nltk.classify.accuracy(classifier,test_set)) )