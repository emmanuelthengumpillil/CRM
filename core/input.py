import valid

def get_name():
    while True:
        name = input("Enter Name:- ")
        if valid.valid_name(name)[1]:
            return {"success":True, "data":name}
        print("Enter alphabet values")

def get_phone():
    while True:
        phone = input("Enter Phone:- ")
        if valid.valid_phone(phone)[1]:
            return {"success":True, "data": phone}


def get_id():
    while True:
        id = input("Enter ID:- ")
        if id.isdigit():
            return {"success":True, "data": id}


def get_input():
    name = get_name()["data"]
    phone = get_phone()["data"]
    list = [name,phone]
    return {"success":True, "data": list}