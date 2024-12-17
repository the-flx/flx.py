def dict_set(dict, key, val):
    if key is None:
        return

    dict[key] = val

    return dict

def dict_get(dict, key):
    if key is None:
        return None

    if not key in dict.keys():
        return None

    return dict[key]

def dict_insert(dict, key, val):
    if not key in dict.keys():
        dict[key] = []

    dict[key].insert(0, val)

    return dict
