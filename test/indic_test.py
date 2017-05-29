# -*- coding: utf-8 -*-

import sys
sys.path.append('/home/vansh/Library/indic_nlp_library/src')

'''
from indicnlp import common, loader
common.set_resources_path('/home/vansh/Library/indic_nlp_resources')

loader.load()
'''

from indicnlp.tokenize import indic_tokenize

import codecs

print "before opening"

with codecs.open('hindi/21_utf8.txt.norm', 'r', encoding='utf8') as f:
    print "after opening"

    data = f.read()

    data = data.replace('\r\n', ' ')
    input_str = data[:10]

    tokenized = indic_tokenize.trivial_tokenize(data[:10])

