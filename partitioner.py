test_list = ['this', 'is','the','first','third','this', 'is','the','second','third','this', 'is','the','third','third',]
print (len(test_list))

def break_into_fractions(broken,fraction):

    for number in range (1,fraction+1):
        broken_copy = list(broken)
        result_set = broken_copy[int(((number-1)*(len(broken_copy)))/fraction):int((number)*(len(broken_copy))/fraction)]
        training_set = broken_copy[0:int((number-1)*(len(broken_copy))/fraction)] + broken_copy[int((number)*(len(broken_copy))/fraction):]
        print("This is the result set, for iteration %s: " % number)
        print(result_set)
        print("This is the training set for iteration %s : " % number)
        print(training_set)

break_into_fractions(test_list,3)

