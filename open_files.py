# This module is to download x bytes from 

import sys
sys.path.append('/home/vansh/Library/indic_nlp_library/src')

from indicnlp.tokenize import indic_tokenize
import codecs
import os 
import random

'''
@Name:      open_x_words

@Desc:      will return a training set and test set of size described by params.
            It first shuffles the list of files in the provided language folder
            and then iterates the first x files such that the overall model set
            size is met.

 @Params:   training_size:  size of trainign set to return
            lang_code:      language code

@Return:    This will return a training set

            This will at least return a training set as large as specified by
            the training_size parameter. It may be off by one file's worth of
            words.

            If the size request is larger than the corpora can provide, it will
            return the maximum corpora's size.

            Also, the output is Non-Deterministic. Meaning with every call to
            open_x_words with the same parameters, it will not return the same
            output. 
'''
def open_x_words(training_size, lang_code):
    
    # the language codes that this accepts
    corpora_dict = {'h': 'hindi', 'm': 'marathi', 'p': 'pali', 's':'sanskrit'}

    param_dir = corpora_dict[lang_code]

    random_files = os.listdir(param_dir)
    random.shuffle(random_files)

    overall_size = training_size
    
    word_list = list()

    for _file in random_files:
        
        if len(word_list) >= overall_size:
            break

        with codecs.open(param_dir + '/' + _file, 'r', encoding='utf8') as f:

            data = f.read()
            data = data.replace('\r\n', ' ')

            tokenized = indic_tokenize.trivial_tokenize(data)

            word_list.extend(tokenized) 

    return word_list

