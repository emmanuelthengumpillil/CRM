import storage


row = {"Name":"qweqw","Phone":"13213"}
f = "crm.csv"

def valid_row_data(row_dict):
    if not isinstance(row_dict, dict):
        return False, None  
    else:
        return True, row_dict

