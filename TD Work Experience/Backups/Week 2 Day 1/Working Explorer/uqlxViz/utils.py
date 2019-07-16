
_validCurrencies = ["USD", "JPY", "EUR", "CAD" ]

def is_currency(x):
    if len(x) != 3:
        return  False
    else:
        return x in _validCurrencies

def is_ccypair(x):
    if len(x) != 6:
        return  False
    else:
        return is_currency(x[0:3]) and is_currency(x[3:6])


def gen_dict_extract(key, var):

    # generalised dictionary extract , find-all-occurrences-of-a-key-in-nested-python-dictionaries-and-lists
    # dcs = list(utils.gen_dict_extract(_dc_key, model_d))

    if hasattr(var,'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result

#def value_ripper(key, structure):

    
                        


def check_exist(tree, key):
    if tree.exists(key) == False:
        return(key)
    else:
        key = key + "1"
        return(check_exist(tree, key))