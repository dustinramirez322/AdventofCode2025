import re

# register dial starting point and dial options
starting_point = 50
dial_options = list(range(100))

# Get input and turn spins into a list
with open('input.txt') as i:
    input_turns = i.read().splitlines()

# reorder list so that the first number is the current point
def determine_current_point(dial_options, starting_point):
    current_point_list = []
    for ad in dial_options[starting_point:]:
        current_point_list.append(ad)
    for zd in dial_options[:starting_point]:
        current_point_list.append(zd)
    return current_point_list


# determine if spin goes right (positive) or left (negative)
# provide output as a negative or positive digit
def spin_direction(input):
    turn_amount = int(re.findall(r"\d+", input)[0])
    # move this to register turn to count large turns
 #   if turn_amount > 100:
 #       turn_amount = turn_amount % 100
    # determine is spin goes left or right and return a value
    if input.startswith('R'):
        return turn_amount
    elif input.startswith('L'):
        return -turn_amount

# determine how many times zero is crossed
def plus_100_adjustment(turn_amount, starting_point, ending_point):
    # determine direction
    if turn_amount < 0:
        # turn is left, if new point is higher than old, zero was crossed
        if ending_point == 0:
            small_zero_turns = 1
        elif starting_point[0] == 0:
            small_zero_turns = 0
        elif ending_point > starting_point[0]:
            small_zero_turns = 1
            print('hello')
        else:
            small_zero_turns = 0
    else:
        # turn is right, if new point is lower than old, zero was crossed
        if ending_point == 0:
            small_zero_turns = 1
        elif starting_point[0] == 0:
            small_zero_turns = 0
        elif ending_point < starting_point[0]:
            small_zero_turns = 1
        else:
            small_zero_turns = 0
    # find total amount of turns
    full_turns = abs(turn_amount) // 100
    total_turns = abs(full_turns + small_zero_turns)
    print(turn_amount, starting_point[0], ending_point, total_turns)
    return total_turns


# register a single turn and return the new current point
def register_turn(current_point_list, turn_amount):
    small_turn = turn_amount % 100
    new_current_point = current_point_list[small_turn]
    return new_current_point


def create_zero_count_list(input):
    # create a blank list to track zeros
    zero_count_list = []
    # define initial starting point of the puzzle
    dial_starting_point = determine_current_point(dial_options, 50)
    for i in input:
        spin_value = spin_direction(i)
        new_current_point = register_turn(dial_starting_point, turn_amount=spin_value)
        zero_crossed_count = plus_100_adjustment(spin_value, dial_starting_point, new_current_point)
        dial_starting_point = determine_current_point(dial_options, starting_point=new_current_point)
        zero_count_list.append(zero_crossed_count)
    return zero_count_list


zero_count_list = create_zero_count_list(input_turns)
print(zero_count_list)
print(sum(zero_count_list))