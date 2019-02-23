import names

def get_random_names(count,gender):
    return_list = []
    if count <= 0:
        return
    for x in range(count):
        return_list.append(names.get_full_name(gender))
    return return_list
