from create_classifier import create_NaiveBayesClassifier
from itertools import combinations

TRAINING_SIZ = 10000000

def create_classifiers(fileName):

	line = '================================================================='
	lang_codes = {'h':'hindi', 's': 'sanskrit', 'm': 'marathi', 'p': 'pali'}

	combos = ['hs', 'ms', 'hp', 'hs', 'hm', 'sp']

	# run classifiers on words as features

	c_list = list()

	print 'features: words'
	for combo in combos:
		classifier, accuracy, size = create_NaiveBayesClassifier(''.join(combo), TRAINING_SIZ)

		print '{:>10}/{:10} epsilon: {:4.3f}\t siz: {:<10}'.format(\
			lang_codes[combo[0]], lang_codes[combo[1]], 1-accuracy, size*2)

		classifier.show_most_informative_features(10)

	print '\n'+line+'\n'

	for n in range(1,7):
		
		print 'features: {}-char grams'.format(n)

		for combo in combos:
			classifier, accuracy, size = create_NaiveBayesClassifier(''.join(combo), \
				TRAINING_SIZ, False, n)

			print '{:>10}/{:10} epsilon: {:4.3f}\t siz: {:<8}'.format(\
				lang_codes[combo[0]], lang_codes[combo[1]], 1-accuracy, size*2)

			classifier.show_most_informative_features()

		print '\n'+line+'\n'
	return


create_classifiers()
