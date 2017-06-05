import nltk
from nltk import *
import random
from io import open
import os.path

'''
@Name:      create_corpora

@Desc:      creates a single, tagged list containing all the words from the
            Hindi, Marathi, Sanskrit and Pali corpora

@Params:    None

@Return:    This will return a shuffled list of all of the words in the Hindi,
            Marathi, Sanskrit and Pali languages.
'''
def create_corpora():
    # Sets the base directory
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "combined_corpora")

    # Read and tag from Hindi corpus
    f = open(os.path.join(base_dir, "hindi", "hindi_data.txt"), encoding="utf-8")
    hindi_corpus = f.read()
    tupled_hindi_words = ([(word, 'hindi') for word in hindi_corpus])
    f.close()

    # Read and tag from Marathi corpus
    g = open(os.path.join(base_dir, "marathi", "marathi_data.txt"), encoding="utf-8")
    marathi_corpus = g.read()
    tupled_marathi_words = ([(word, 'marathi') for word in marathi_corpus])
    g.close()

    # Read and tag from Sanskrit corpus
    h = open(os.path.join(base_dir, "sanskrit", "sanskrit_data.txt"), encoding="utf-8")
    sanskrit_corpus = h.read()
    tupled_sanskrit_words = ([(word, 'sanskrit') for word in sanskrit_corpus])
    h.close()

    # Read and tag from Pali corpus
    i = open(os.path.join(base_dir, "pali", "pali_data.txt"), encoding="utf-8")
    pali_corpus = i.read()
    tupled_pali_words = ([(word, 'pali') for word in pali_corpus])
    i.close()

    # Combines all of the words and shuffles
    combined_corpora = tupled_hindi_words + tupled_marathi_words + tupled_sanskrit_words + tupled_pali_words
    random.shuffle(combined_corpora)

    return combined_corpora
