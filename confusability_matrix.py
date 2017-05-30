from create_classifier import *
def print_matrix():
	print "Language to be compared with"
	print "\tsanskrit\tpali"

	print " words"
	print "Hindi\t" + str(1-create_NaiveBayesClassifier('hs',1000000)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('hp',1000000)[1])[:5]
	print "Marathi\t" + str(1-create_NaiveBayesClassifier('ms',1000000)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('mp',1000000)[1])[:5]

	print "\n 1 character grams"
	print "Hindi\t" + str(1-create_NaiveBayesClassifier('hs',1000000, False, 1)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('hp',1000000, False, 1)[1])[:5]
	print "Marathi\t" + str(1-create_NaiveBayesClassifier('ms',1000000, False, 1)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('mp',1000000, False, 1)[1])[:5]

	print "\n 2 character grams"
	print "Hindi\t" + str(1-create_NaiveBayesClassifier('hs',1000000, False, 2)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('hp',1000000, False, 2)[1])[:5]
	print "Marathi\t" + str(1-create_NaiveBayesClassifier('ms',1000000, False, 2)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('mp',1000000, False, 2)[1])[:5]

	print "\n 3 character grams"
	print "Hindi\t" + str(1-create_NaiveBayesClassifier('hs',1000000, False, 3)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('hp',1000000, False, 3)[1])[:5]
	print "Marathi\t" + str(1-create_NaiveBayesClassifier('ms',1000000, False, 3)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('mp',1000000, False, 3)[1])[:5]

	print "\n 4 character grams"
	print "Hindi\t" + str(1-create_NaiveBayesClassifier('hs',1000000, False, 4)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('hp',1000000, False, 4)[1])[:5]
	print "Marathi\t" + str(1-create_NaiveBayesClassifier('ms',1000000, False, 4)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('mp',1000000, False, 4)[1])[:5]

	print "\n 5 character grams"
	print "Hindi\t" + str(1-create_NaiveBayesClassifier('hs',1000000, False, 5)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('hp',1000000, False, 5)[1])[:5]
	print "Marathi\t" + str(1-create_NaiveBayesClassifier('ms',1000000, False, 5)[1])[:5] + '\t\t' + str(1-create_NaiveBayesClassifier('mp',1000000, False, 5)[1])[:5]

print_matrix()