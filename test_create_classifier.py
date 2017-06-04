# -*- coding: utf-8 -*-

from create_classifier import create_NaiveBayesClassifier

c, a, s = create_NaiveBayesClassifier('mpsh', 20000)
c.show_most_informative_features(-10)
print a
