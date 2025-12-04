import valid

def get_name():
    while True:
        name = input("Enter Name:- ")
        if name.isalpha():
            return 200, name
        print("Enter alphabet values")

def get_phone():
    while True:
        phone = input("Enter Phone:- ")
        if phone.isnumeric() and 10 <= (len(phone)) <= 12:
            return 200, phone
        return 400, None


def create_row_dict(file):
    keys = ["Name", "Phone"]
    values = [get_name()[1], get_phone()[1]]
    row_dict = dict(zip(keys, values))
    if valid.validate_row(file, row_dict):
        return 200, row_dict

print(create_row_dict("crm.csv"))