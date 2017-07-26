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
    answer_set=set([()])
    hand_len=len(hand)
    list_hand=list(hand)
    all_idx=gen_all_sequences((0,1),hand_len)
    for each_idx in all_idx:
        temp_answer=[]
        
        for each_num in range(hand_len):
        
     
            if each_idx[each_num]==1:
                add_item=list_hand[each_num]
                temp_answer.append(add_item)
          
                answer_set.add(tuple(temp_answer))
    return answer_set
print gen_all_holds((1,2,4))
