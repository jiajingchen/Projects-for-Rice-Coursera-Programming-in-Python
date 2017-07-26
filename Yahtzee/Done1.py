"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)

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



def max_repeats(seq):
    """
    Compute the maxium number of times that an outcome is repeated
    in a sequence
    """
    item_count = [seq.count(item) for item in seq]
    return max(item_count)

def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score 
    """
    each_box=[int(item)*hand.count(item) for item in hand]
    return max(each_box)


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    outcomes=[item for item in range(1,num_die_sides+1)]
    print outcomes
    all_outcomes=gen_all_sequences(outcomes, num_free_dice)
    sum_outcomes=0.0
    for seq in all_outcomes:
        sum_outcomes+=score(seq)
    return sum_outcomes/len(all_outcomes)
print expected_value((1,1), 6,4)

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



def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_expected=0.0
    max_choice=[]
    for choice in gen_all_holds(hand):
        held_dice=choice
        num_free_dice=len(hand)-len(held_dice)
        current_expected=expected_value(held_dice, num_die_sides, num_free_dice)
        if current_expected>= max_expected:
            max_expected= current_expected
            max_choice=list(choice)
    return_tuple=tuple(max_choice)        
    return (max_expected, return_tuple)


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
    
    
run_example()


#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
                                       
    
    
    

