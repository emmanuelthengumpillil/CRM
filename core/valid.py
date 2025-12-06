import storage


row = {"Name":"jkljk","Phone":"13213"}
row2 = {"Phone":"132465","Name":"qweqw"}
f = "crm.csv"


def valid_row_data(row_dict):
    if not isinstance(row_dict, dict):
        return 404, False, None  
    return 200, True, row_dict


def validate_keys(file, row_dict):
    header = storage.read_csv(file)[2]
    # set() will ignore it from checking the order
    if header == None:
        return 405, False, None
    if not set(header) == set(row_dict.keys()):
        return 405, False, None
    return 200, True, row_dict


def validate_not_empty(row_dict):
    values = list(row_dict.values())
    for i in range(len(row_dict)):
        if values[i] == "" or values[i] is None:
            return 404, False, None
    return 200, True, row_dict


def validate_row(file,row_dict):
    if valid_row_data(row_dict)[1]:
        if validate_keys(file, row_dict)[1]:
            if validate_not_empty(row_dict)[1]:
                return 200, True, row_dict
            return 404, False, None
        return 404, False, None
    return 404, False, None


def valid_name(name):
    if str(name).isalpha() and not "":
        return 200, True, name
    return 405, False, None


def valid_phone(phone):
    if str(phone).isdigit and not "":
        return 200, True, phone
    return 405, False, None