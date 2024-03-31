from functools import reduce
from .remove_garbage import remove_garbage

def get_last_n_items_safe(lst, n):
    if len(lst) >= n:
        return lst[-n:]
    else:
        return lst[:]

def combine_last_n_elements(lst, n, splitter=" "):
    if len(lst) >= n:
        last_n_combined = splitter.join(lst[-n:])
        return lst[:-n] + [last_n_combined]
    else:
        return lst

def pull_possible_apns_from_cell_value(cell_value):
    cell_value = remove_garbage(cell_value)
    cell_value_split = cell_value.split(" ")
    cell_value_split = [s for s in cell_value_split if len(s) != 1 and len(s) != 2] # Remove one and two character strings
    new_strings = []

    # if ('415301302' in cell_value):
    #     print('great: ' + str(cell_value))

    for index, val in enumerate(cell_value_split):
        val = val.strip()
        new_strings.append(val)
        last_items_2 = get_last_n_items_safe(new_strings, 2)
        last_items_3 = get_last_n_items_safe(new_strings, 3)

        if len(last_items_3) == 3:
            sum_result = reduce(lambda x, y: x + str(len(y)), last_items_3, "")
            if sum_result == "323":
                new_strings = combine_last_n_elements(new_strings, 3)
                
        if len(last_items_2) == 2:
            # try:
            #     if last_items_2[0][-1] == "-" and len(last_items_2[1]) == 3:
            #         huh = last_items_2[0][-1]
            # except Exception as e:
            if len(last_items_2[0]) > 0 and last_items_2[0][-1] == "-" and len(last_items_2[1]) == 3:
                new_strings = combine_last_n_elements(new_strings, 2, "")
                # print(new_strings[-1])

    # if ('415301302' in cell_value):
    #     print('great 2: ' + str(cell_value))
    #     print(new_strings)
    
    if len(new_strings) == 2:
        new_strings = [" ".join(new_strings)]

        
    return new_strings