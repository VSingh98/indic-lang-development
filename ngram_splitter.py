'''
@Name:      ngram

@Desc:      splits a word into its ngram parts, given by gramsize

@Params:    string:      word to split into ngrams
            gramsize:    size of each ngram

@Return:    A tuple of ngrams for that word

            For example:
            ngram("stop", 2)
            [st, to, op]
'''
def ngram(string,gramsize):
    ngrams_list =[]
    for number in range(len(string)):
        if len(string[number:number+gramsize]) == gramsize:
            ngrams_list.append(string[number:number+gramsize])
    return ngrams_list