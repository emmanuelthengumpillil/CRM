import storage


row = {"Name":"qweqw","Phone":"13213"}
row2 = {"Phone":"13213","Name":"qweqw"}
f = "crm.csv"


def valid_row_data(row_dict):
    if not isinstance(row_dict, dict):
        return False, None  
    else:
        return True, row_dict, None


def validate_keys(file, row_dict):
    header = storage.read_csv(file)[2]
    # set() will ignore it from checking the order
    if not set(header) == set(row_dict.keys()):
        return 405, False, None
    return 200, True, row_dict, None


def validate_not_empty(row_dict):
    values = set(row_dict.values())
    if values == "" or values is None:
        return 404, False, None
    return 200, True, None
