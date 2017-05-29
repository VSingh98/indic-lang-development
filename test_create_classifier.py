# -*- coding: utf-8 -*-

from create_classifier import create_NaiveBayesClassifier

c, a = create_NaiveBayesClassifier('spm', 2000)
print a

print c.classify({'feature':'पाळण्यात असल्यापासून या अद्भुताचे त्याला'})

d, b = create_NaiveBayesClassifier('m', 2000, flag=False, n=2)

print b

print d.classify({'feature':'पाळण्यात असल्यापासून या अद्भुताचे त्याला'})

