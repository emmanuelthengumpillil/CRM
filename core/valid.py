import storage


row = {"Name":"jkljk","Phone":"13213"}
row2 = {"Phone":"132465","Name":"qweqw"}
f = "crm.csv"


def valid_row_data(row_dict):
    if not isinstance(row_dict, dict):
        return False
    return True


def validate_keys(file, row_dict):
    header = storage.read_csv(file)["header"]
    # set() will ignore it from checking the order
    if header == None:
        return False
    if set(header) != set(row_dict.keys()):
        return False
    return True


def validate_not_empty(row_dict):
    # values = list(row_dict.values())
    for i in row_dict.values():
        if i == "" or i == None:
            return False
    return True


def validate_row(file,row_dict):
    if valid_row_data(row_dict):
        if validate_keys(file, row_dict):
            if validate_not_empty(row_dict):
                return {"success": True, "data": row_dict}
            return {"success": False, "error": "row_dict is empty"}
        return {"success": False, "error": "key is not valid"}
    return {"success": False, "error": "row_data invalid"}


def valid_name(name):
    if str(name).isdigit() == False:
        return {"success":True,"data": name}
    return {"success": False, "error": "Name is not valid"}


def valid_phone(phone):
    if str(phone).isdigit() and phone != "":
        if 10 <= len(phone) <= 12:
            return {"success":True,"data": phone}
    return {"success": False, "error": "Phone Number is not valid"}