
           


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
    answer_set = set([()])
    for idx in range(len(hand)):
        new_gen= gen_all_sequences(hand, idx)
    answer_set.add(tuple(new_gen))
    print answer_set
gen_all_holds((1,2,3))
