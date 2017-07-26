


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
            used_index=[]
            for used_item in partial_sequence:
                
                used_index.append(used_item)

                #print used_index
            for item in hand:
                if item not in used_index:
                    #print "item",item
                    
                    new_sequence = list(partial_sequence)
                    new_sequence.append(item)
                    temp_set.add(tuple(new_sequence))
                    all_set.add(tuple(new_sequence))
                    #print "temp_set",temp_set
          
        answer_set = temp_set
        
        #print "answer_set",answer_set
        #print 'all_set',all_set
    return all_set
print (gen_all_holds((1,2)))
print type(gen_all_holds((1,2,3)))
