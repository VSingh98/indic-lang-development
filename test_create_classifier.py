# -*- coding: utf-8 -*-

from create_classifier import create_NaiveBayesClassifier

c, a = create_NaiveBayesClassifier('hm', 2000)
print a

print c.classify({'word':'सब'})

d, b = create_NaiveBayesClassifier('hm', 2000, flag=False, n=4)

print b

print d.classify({'word':'सब'})

