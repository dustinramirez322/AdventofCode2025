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


# split each product id in half and determine if they match
def prod_id_split(prod_id):
    # determine the length of the prod id
    prod_id_length = len(str(prod_id))
    # split in half to determine sides to compare
    half_size = int(prod_id_length/2)
    prod_id_first_half = str(prod_id)[half_size:]
    prod_id_sec_half = str(prod_id)[:half_size]
    # determine if match occurs
    if prod_id_first_half == prod_id_sec_half:
        return True
    else:
        return False

    pass


# add matching prod ids
def create_match_prod_ids_list(prod_id, prod_half_match):
    if prod_half_match == True:
        return prod_id

def find_and_add_prod_ids(input):
    matching_list = []
    for i in input:
        prod_id_list = avail_prod_ids(i)
        for p in prod_id_list:
            match = prod_id_split(p)
            if match is True:
                matching_list.append(p)
    answer = sum(matching_list)
    return answer

answer = find_and_add_prod_ids(input)
print(answer)