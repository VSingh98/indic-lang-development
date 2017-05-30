from create_classifier import create_NaiveBayesClassifier
from itertools import combinations

TRAINING_SIZ = 1000000

def create_classifiers():

	lang_codes = {'h':'hindi', 's': 'sanskrit', 'm': 'marathi', 'p': 'pali'}

	# create generator to find all combinations of the language codes
	generator = combinations(lang_codes.keys(), 2)
	combos = list()

	# fill combos with values from generator
	for element in generator:
		combos.append(''.join(element))

	# run classifiers on words as features
	print 'features: words'
	for combo in combos:
		classifier, accuracy, size = create_NaiveBayesClassifier(''.join(combo), TRAINING_SIZ)

		print '{:>10}/{:10} epsilon: {:4.3f}\t siz: {:<10}'.format(\
			lang_codes[combo[0]], lang_codes[combo[1]], 1-accuracy, size*2)

	print '\n'

	for n in range(1,7):
		
		print 'features: {}-char grams'.format(n)

		for combo in combos:
			classifier, accuracy, size = create_NaiveBayesClassifier(''.join(combo), \
				TRAINING_SIZ, False, n)

			print '{:>10}/{:10} epsilon: {:4.3f}\t siz: {:<8}'.format(\
				lang_codes[combo[0]], lang_codes[combo[1]], 1-accuracy, size*2)

		print '\n'
	return


	'''
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
	'''
	
create_classifiers()