with open('input.txt') as i:
    batteries = i.read().splitlines()


# create jolt
def create_jolt_val_list():
    # create list with values
    joltage_val_list = list(range(10))
    # reverse the list so its high to low
    joltage_val_list.reverse()
    # single digit values from list
    joltage_val_list.pop()
    return joltage_val_list

    

# find the largest number from left to right
def find_jolt_tens(joltage_val_list, battery):
    # find the first largest number
    for joltage in joltage_val_list:
        # assign x as a value to track what position the first val was found
        x = 0
        # iterate over the battery, but skip the final digit
        for b in battery[:-1]:
            # find a match and covert battery placeholder into int for the time being
            if joltage == int(b):
                joltage_tens = b
                # once the largest value is found, break
                break
            x += 1
        # once joltage tens place has been found, break out of the loop
        if 'joltage_tens' in locals():
            break
    return {'value': joltage_tens, 'position': int(x)}


# search for the ones place using the position taken from the find_jolt_tens function
def find_jolt_ones(joltage_val_list, battery, position):
    # find the largest number starting after the position from the find_jolts_ten_function
    for joltage in joltage_val_list:
        # set the position to start in the battery value after where the tens digit was found
        for b in battery[position + 1:]:
            if joltage == int(b):
                joltage_ones = b
                # break once a value is found
                break
        if 'joltage_ones' in locals():
            break
    return joltage_ones


joltage_val_list = create_jolt_val_list()
joltage_solution_list = []
for battery in batteries:
    joltage_tens_info = find_jolt_tens(joltage_val_list, battery)
    joltage_tens = joltage_tens_info['value']
    position = joltage_tens_info['position']
    joltage_ones = find_jolt_ones(joltage_val_list, battery, position)
    joltage_value = int(joltage_tens + joltage_ones)
    joltage_solution_list.append(joltage_value)

print(sum(joltage_solution_list))