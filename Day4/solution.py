with open('input.txt') as i:
    rows = i.read().splitlines()
    # add .. to front and back of each row
    rows = [f"..{row}.." for row in rows]
    # append and prepend list to account for first and last rows
    row_len = len(rows[0])
    rows.append(row_len * '.')
    rows = [row_len * '.'] + rows



# function to find a roll

def find_paper_roll(rows, roll_count=[]): 
    row_num = 0
    for row in rows:
        column_num = 0
        for r in row:
            # iterate over each row and search for '@'
            if r == '@':
                # if found, eval the nine adjacent locations and add 1 to the roll_count list
                roll_count.append(eval_adj_locs(row_num, column_num, rows))
            column_num += 1
        row_num += 1
    
    return roll_count



# function to evaluate adjacent spaces
def eval_adj_locs(row_num, column_num, rows):
    # set the eval range
    eval_top = rows[row_num - 1][column_num - 1: column_num + 2]
    eval_mid = rows[row_num][column_num - 1: column_num + 2]
    eval_bot = rows[row_num + 1][column_num - 1: column_num + 2]
    # count how many @s exist
    count_top = eval_top.count('@')
    count_mid = eval_mid.count('@')
    count_bot = eval_bot.count('@')
    total = count_top + count_mid + count_bot
    # if total is less than 5, return this position as "selectable in the puzzle"
    if total < 5:
        return 1
    else:
        return 0



roll_count = find_paper_roll(rows, roll_count=[])
print(sum(roll_count))