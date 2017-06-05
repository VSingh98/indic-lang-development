larger_set = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20 ]
for element in larger_set:
    element = str(element)

smaller_set = ['a','b','c','d','e']

# So, det_set refers to the determining set. that's the set that decides how big the partitions will be.
# so if we do a tenth of the det_set, in this case, we'll be making 'test sets' of a size of 2
def partition_so_many_times(det_set,indet_set,fraction):
    word_count = int(len(det_set)/fraction)
    for number in range (1,fraction+1):
        start_point = word_count*(number-1)
        end_point = word_count*(number)
        # ok so, here I'm just adding the determining set on to the test set. this is the easy part.
        test_set = det_set[start_point:end_point]

        """ ok now we have to deal with the smaller set. so, I'm putting in these multiple things so that we can
        ultimately figure out what the slices should be. imagien if on the bigger list we are going from,
        I don't know, 240 to 250. and let's say the smaller list is like, only 100 elements long.
        then we want to remove the length of the smaller list twice from the starting and ending points, giving us
        fourty and fifty, rather than two hundred and fourty and two hundred and fifty. """

        end_point_multiple = int(int(end_point) / len(indet_set))
        start_point_multiple = int(int(start_point) / len(indet_set))
        start_point = start_point-len(indet_set)*start_point_multiple
        end_point = end_point- len(indet_set)*end_point_multiple

        # we need to see if we need clipping. we are clipping if we the edges of the list need to be in the test set.
        if end_point < start_point:
            test_set += indet_set[start_point:]
            test_set += indet_set[:end_point]
        elif end_point >= start_point:
            test_set += indet_set[start_point:end_point]
        print ("this is the test set for iteration %s" %number)
        print(test_set)
partition_so_many_times(larger_set,smaller_set,10)