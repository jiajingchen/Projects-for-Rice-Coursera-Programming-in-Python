def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    hand_set = set([tuple(hand)])
    all_answer_set=set([()])
    for dummy_idx in range(len(hand)):
        iteration_set = set()
        for partial_sequence in all_answer_set:
            
            for item in hand:
                print "item",item
                if item in partial_sequence:
                    temp_set = set()
                    temp_list= list(partial_sequence)
                    temp_list.remove(item)
                    temp_set=set(temp_list)
                    print "temp_set",temp_set
            
                    all_answer_set.add(tuple(temp_set))
                    print "answer_set",all_answer_set
        
gen_all_holds((1,2,3))
