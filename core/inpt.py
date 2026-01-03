import valid

def get_name():
    while True:
        name = input("Enter Name:- ")
        if valid.valid_name(name)["success"]:
            return {"success":True, "data":name}
        print("Enter alphabet values")

def get_phone():
    while True:
        phone = input("Enter Phone:- ")
        if valid.valid_phone(phone)["success"]:
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


def get_choice():
    ch = ["add","remove","update","search","view"]
    while True:
        choice = input("ADD / REMOVE / UPDATE / SEARCH / VIEW :- ").lower()
        for i in range(len(ch)):
            if choice == ch[i]:
                return {"success":True, "data": choice}
        print("== Please enter among the following choices ==")


def get_file():
    while True:
        file = input("get file name:- ")
        if valid.valid_name(file):
            return {"success": True, "data": file}