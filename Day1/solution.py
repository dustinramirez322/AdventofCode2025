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
    if turn_amount > 100:
        turn_amount = turn_amount % 100
    # determine is spin goes left or right and return a value
    if input.startswith('R'):
        return turn_amount
    elif input.startswith('L'):
        return -turn_amount

def plus_100_adjustment():
    pass

# register a single turn and return the new current point
def register_turn(current_point_list, turn_amount):
    new_current_point = current_point_list[turn_amount]
    return new_current_point

# create list of new turn by turn locations
def create_ending_location_list(input):
    # define initial starting point of the puzzle
    dial_starting_point = determine_current_point(dial_options, 50)
    # create blank list that tracks current positions
    dial_ending_location = []
    # begin spinning the dial
    for i in input:
        spin_value = spin_direction(i)
        new_current_point = register_turn(dial_starting_point, turn_amount=spin_value)
        dial_starting_point = determine_current_point(dial_options, starting_point=new_current_point)
        dial_ending_location.append(new_current_point)
    return dial_ending_location

ending_location_list = create_ending_location_list(input_turns)
print(ending_location_list.count(0))

