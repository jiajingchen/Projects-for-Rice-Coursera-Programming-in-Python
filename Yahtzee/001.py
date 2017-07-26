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

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = set([tuple(hand)])
    all_answer_set=set([()])
    for dummy_idx in range(len(hand)):
        temp_set = set()
        
        for partial_sequence in answer_set:
            print "partial_sequence",partial_sequence
            print "answer_set",answer_set
            for item in hand:
                new_sequence = list(partial_sequence)
                all_sequence=list(hand)
                print "item",item
                print "new_sequence",new_sequence
                if item in hand:
                    all_sequence.remove(item)
                    temp_set.add(tuple(all_sequence))
                    print "all_sequence",all_sequence
        answer_set = temp_set
        all_answer_set.add(tuple(answer_set))
    return all_answer_set

print gen_all_holds((1,2,3))
