def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    all_set=set([()])
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
                print "temp_set",temp_set
        answer_set = temp_set
        all_set.add(tuple(answer_set))
        print "answer_set",answer_set
        print 'all_set',all_set
    return answer_set
print gen_all_sequences((1,2,3),3)
