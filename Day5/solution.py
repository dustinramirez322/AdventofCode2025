with open('input.txt') as i:
    ing_ids = i.read().splitlines()

with open('ranges.txt') as j:
    fresh_ids = j.read().splitlines()

# split fresh ids into lists of available options
def fresh_range_split(fresh_id_range):
    split_range = fresh_id_range.split('-')
    fresh_range = range(int(split_range[0]), int(split_range[1]) + 1)
    return fresh_range

# search for ingredient id in split ranges
def search_in_ranges(ing_ids, fresh_ids):
    fresh_id_count = []
    for ing_id in ing_ids:
        for fresh_id in fresh_ids:
            fresh_range = fresh_range_split(fresh_id)
            if int(ing_id) in fresh_range:
                fresh_id_count.append(1)
                break
    return(fresh_id_count)


answer = search_in_ranges(ing_ids, fresh_ids)
print(sum(answer))