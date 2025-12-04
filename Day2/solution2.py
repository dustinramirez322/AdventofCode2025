with open('input.txt') as i:
    input = i.readline().split(',')

# create list of available product ids
def avail_prod_ids(prod_id):
    prod_id_list = []
    # split prod id to get first and last prod ids
    start_end_prod_id = prod_id.split('-')
    # create a list of all prod ids between first and last ids
    prod_id_list = list(range(int(start_end_prod_id[0]), int(start_end_prod_id[1]) + 1))
    return prod_id_list


# determine factors options for prod_id length
def prod_id_split(prod_id):
    # determine the length of the prod id
    prod_id_length = len(str(prod_id))
    # determine available divisible lengths
    factors = []
    for r in range(1, prod_id_length +1):
        # don't add the prod_id_length since it won't match itself
        if r == prod_id_length:
            pass
        elif prod_id_length % r == 0:
            factors.append(r)
    return factors


# check each factor size for matches
def factor_match_check(prod_id, factors):
    # make an empty list to track prod_id matches
    prod_id_matching_list = []
    for f in factors:
        # make an empty list to house the split product id
        sliced_list = []
        for r in range(0, len(str(prod_id)), f):
            # split the product id into however many parts
            slice_part = str(prod_id)[r:r + f]
            # add those to the sliced list so we can compare them
            sliced_list.append(int(slice_part))
        # convert to a set so we can check for same/ duplicate values
        set_test = len(set(sliced_list))
        # if only one value is in the set, each portion matches one another
        if set_test == 1:
            print(sliced_list)
            prod_id_matching_list.append(prod_id)
            # break out once a match is found to prevent prod_ids being counted twice
            # ie:  222222 matching as 2,2,2,2,2 and 22,22,22 and 222,222
            break
    return prod_id_matching_list


def find_and_add_prod_ids(input):
    matching_list = []
    for i in input:
        prod_id_list = avail_prod_ids(i)
        for p in prod_id_list:
            factors = prod_id_split(p)
            matching_prod_id_list = factor_match_check(p, factors)
            for m in matching_prod_id_list:
                matching_list.append(m)
    answer = sum(matching_list)
    return answer

answer = find_and_add_prod_ids(input)
print(answer)