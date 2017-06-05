# -*- coding: utf-8 -*-
from indicnlp.tokenize import indic_tokenize

indic_text=u'खराखुरा'

print indic_text.split()

tokenized = indic_tokenize.trivial_tokenize(indic_text)

print tokenized