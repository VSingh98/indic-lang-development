import sys
sys.path.append('/home/vansh/Library/indic_nlp_library/src')

from indicnlp import common, loader
common.set_resources_path('/home/vansh/Library/indic_nlp_resources')

loader.load()