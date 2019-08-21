def mean(num_list):
    assert type(num_list) == list
    if len(num_list) == 0:
        raise Exception("don't pass in empty lists!")
    else: return sum(num_list)/len(num_list)
