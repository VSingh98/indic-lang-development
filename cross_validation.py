import nltk
from nltk import *

from create_classifier import *
import numpy as np
from open_files import *



def cross_validate(feature_list, fraction):
    # List to keep track of accuracy counts
    accuracy_list = []
    mean = 0;

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
    #print accuracy_list

    return (mean, standard_deviation)

#cross_validate(getAllfeatures("hs", False, 1))
#cross_validate(getAllfeatures("hs"))
