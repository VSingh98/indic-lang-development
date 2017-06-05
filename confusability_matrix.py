from create_classifier import create_NaiveBayesClassifier
from itertools import combinations
from cross_validation import cross_validate
from open_files import getAllfeatures
import codecs

'''
def create_classifiers(fileName, showFeatures=False):

	line = '================================================================='
	lang_codes = {'h':'hindi', 's': 'sanskrit', 'm': 'marathi', 'p': 'pali'}

	combos = ['hs', 'ms', 'hp', 'hs', 'hm', 'sp']

	# run classifiers on words as features

	c_list = list()

	with codecs.open(fileName, "w", encoding='utf8') as f:

		f.write('features: words\n')
		for combo in combos:
			classifier, accuracy, size = create_NaiveBayesClassifier(''.join(combo), TRAINING_SIZ)

			f.write('{:>10}/{:10} epsilon: {:4.3f}\t siz: {:<10}\n'.format(\
				lang_codes[combo[0]], lang_codes[combo[1]], 1-accuracy, size*2))

			if showFeatures:
				informative_features = str(classifier.show_most_informative_features())
				f.write(informative_features + '\n')

			f.write('\n'+line+'\n')

		for n in range(1,7):
			
			f.write('features: {}-char grams\n'.format(n))

			for combo in combos:
				classifier, accuracy, size = create_NaiveBayesClassifier(''.join(combo), \
					TRAINING_SIZ, False, n)

				f.write('{:>10}/{:10} epsilon: {:4.3f}\t siz: {:<8}\n'.format(\
					lang_codes[combo[0]], lang_codes[combo[1]], 1-accuracy, size*2))

				if showFeatures:
					informative_features = str(classifier.show_most_informative_features())
					f.write(informative_features + '\n')

				f.write('\n'+line+'\n')
'''

def create_classifiers(fileName):

	line = '================================================================='
	lang_codes = {'h':'hindi', 's': 'sanskrit', 'm': 'marathi', 'p': 'pali'}

	combos = ['hs', 'ms', 'hp', 'mp']

	# run classifiers on words as features

	c_list = list()

	with codecs.open(fileName, "w", encoding='utf8') as f:

		f.write('features: words\n')
		for combo in combos:
			mean, stdev = cross_validate(getAllfeatures(combo), 5)

			f.write('{:>10}/{:10} mean epsilon: {:4.3f}\t stdev: {:6.5f}\n'.format(\
				lang_codes[combo[0]], lang_codes[combo[1]], 1-mean, stdev))

		f.write('\n'+line+'\n')

		for n in range(2,3):
			
			f.write('features: {}-char grams\n'.format(n))

			for combo in combos:
				mean, stdev = cross_validate(getAllfeatures(combo, False, n), 5)

				f.write('{:>10}/{:10} mean epsilon: {:4.3f}\t stdev: {:6.5f}\n'.format(\
					lang_codes[combo[0]], lang_codes[combo[1]], 1-mean, stdev))

			f.write('\n'+line+'\n')


create_classifiers("program3.data")