from create_classifier import *
def print_matrix():
    print "Language to be compared with\tsanskrit\tpali"
    print "Hindi\t" + str(create_NaiveBayesClassifier('hs',1000)[1]) + '\t' + str(create_NaiveBayesClassifier('hp',1000)[1])
    print "Marathi\t" + str(create_NaiveBayesClassifier('ms',1000)[1]) + '\t' + str(create_NaiveBayesClassifier('mp',1000)[1])
print print_matrix()