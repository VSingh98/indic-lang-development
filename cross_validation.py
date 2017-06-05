import nltk
from nltk import *

from create_classifier import *
import numpy as np
from open_files import *

'''
@Name:      create_corpora

@Desc:      creates a single, tagged list containing all the words from the
            Hindi, Marathi, Sanskrit and Pali corpora

@Params:    gram_count: the size of the ngram we would like to split for each word

@Return:    This will return a shuffled list of all of the words in the Hindi,
            Marathi, Sanskrit and Pali languages.
'''
'''
def create_corpora(gram_count=2):
    # Sets the base directory
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "combined_corpora")

    # Read and tag from Hindi corpus
    f = open(os.path.join(base_dir, "hindi", "hindi_data.txt"), encoding="utf-8")
    hindi_corpus = f.read()
    tokenized_hindi_corpus = hindi_corpus.split()
    hindi_ngrams = []
    for word in tokenized_hindi_corpus:
        hindi_ngrams += ngram(word, gram_count)
    tupled_hindi_words = ([(word, 'hindi') for word in hindi_ngrams])
    f.close()

    # Read and tag from Marathi corpus
    g = open(os.path.join(base_dir, "marathi", "marathi_data.txt"), encoding="utf-8")
    marathi_corpus = g.read()
    tokenized_marathi_corpus = marathi_corpus.split()
    marathi_ngrams = []
    for word in tokenized_marathi_corpus:
        marathi_ngrams += ngram(word, gram_count)
    tupled_marathi_words = ([(word, 'marathi') for word in marathi_ngrams])
    g.close()

    # Read and tag from Sanskrit corpus
    h = open(os.path.join(base_dir, "sanskrit", "sanskrit_data.txt"), encoding="utf-8")
    sanskrit_corpus = h.read()
    tokenized_sanskrit_corpus = sanskrit_corpus.split()
    sanskrit_ngrams = []
    for word in tokenized_sanskrit_corpus:
        sanskrit_ngrams += ngram(word, gram_count)
    tupled_sanskrit_words = ([(word, 'sanskrit') for word in sanskrit_ngrams])
    h.close()

    # Read and tag from Pali corpus
    i = open(os.path.join(base_dir, "pali", "pali_data.txt"), encoding="utf-8")
    pali_corpus = i.read()
    tokenized_pali_corpus = pali_corpus.split()
    pali_ngrams = []
    for word in tokenized_pali_corpus:
        pali_ngrams += ngram(word, gram_count)
    tupled_pali_words= ([(word, 'pali') for word in pali_ngrams])
    i.close()

    # Combines all of the words and shuffles
    combined_corpora = tupled_hindi_words + tupled_marathi_words + tupled_sanskrit_words + tupled_pali_words
    random.shuffle(combined_corpora)

    return combined_corpora
'''

def cross_validate(feature_list):
    # List to keep track of accuracy counts
    accuracy_list = []
    mean = 0;

    fraction = 10
    # Splice at 10% and run down each row.
    for number in range (1,fraction+1):
        print "starting set"
        # Break into
        broken_copy = list(feature_list)
        test_set = broken_copy[int(((number-1)*(len(broken_copy)))/fraction):int((number)*(len(broken_copy))/fraction)]
        training_set = broken_copy[0:int((number-1)*(len(broken_copy))/fraction)] + broken_copy[int((number)*(len(broken_copy))/fraction):]

        accuracy_list += [ create_NaiveBayesClassifier(test_set, training_set)[1] ]
        print "finished set: " + str(number)

    mean = np.mean(accuracy_list)
    standard_deviation = np.std(accuracy_list, ddof=1)
    print accuracy_list
    return {mean, standard_deviation}

#cross_validate(getAllfeatures("hs", False, 1))
cross_validate(getAllfeatures("hs"))
