import storage


row = {"Name":"qweqw","Phone":"13213"}
f = "crm.csv"

def valid_row_data(row_dict):
    if not isinstance(row_dict, dict):
        return False, None  
    else:
        return True, row_dict

def validate_keys(file, row_dict):
    count = 0
    header = storage.read_csv(file)[2]
    key_list = list(row_dict.keys())
    for i in range(len(header)):
        if header[i] == key_list[i]:
            pass
        else:
            count += 1
    if count != 0:
        return False, None
    else:
        return True, row_dict
