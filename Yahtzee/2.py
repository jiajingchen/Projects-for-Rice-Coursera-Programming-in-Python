def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set
print gen_all_sequences((1,2,3),2)

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    all_set=set([()])
    answer_set = set([()])
    for dummy_idx in range(len(hand)):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in hand:
                if item not in list(answer_set)[:dummy_idx+1][:]:
                    print "tiem",item
                    print list(answer_set)[:dummy_idx+1][:]
                    new_sequence = list(partial_sequence)
                    new_sequence.append(item)
                    temp_set.add(tuple(new_sequence))
                    all_set.add(tuple(new_sequence))
                    print "temp_set",temp_set
        answer_set = temp_set
        
        print "answer_set",answer_set
        #print 'all_set',all_set
    return all_set
print gen_all_holds((1,2))
