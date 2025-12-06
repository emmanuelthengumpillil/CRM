import valid

def get_name():
    while True:
        name = input("Enter Name:- ")
        if valid.valid_name(name)[1]:
            return 200, True, name
        print("Enter alphabet values")

def get_phone():
    while True:
        phone = input("Enter Phone:- ")
        if valid.valid_phone(phone)[1]:
            return 200, True, phone


def get_id():
    while True:
        id = input("Enter ID:- ")
        if id.isdigit():
            return 200, True, id


def create_row_dict(file):
    keys = ["Name", "Phone"]
    values = [get_name()[1], get_phone()[1]]
    row_dict = dict(zip(keys, values))
    if valid.validate_row(file, row_dict):
        return 200, row_dict


print(get_id())