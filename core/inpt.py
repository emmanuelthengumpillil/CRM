import valid
import sys

def get_name():
    while True:
        name = input("Enter Name:- ")
        if valid.valid_name(name)["success"]:
            return {"success": True, 
                "data": name, 
                "error" : None}
        print("Enter alphabet values")


def get_phone():
    while True:
        phone = input("Enter Phone:- ")
        if valid.valid_phone(phone)["success"]:
            return {"success": True, 
                "data": phone, 
                "error" : None}


def get_id():
    while True:
        id = input("Enter ID:- ")
        if id.isdigit():
            return {"success": True, 
                "data": id, 
                "error" : None}


def get_input():
    name = get_name()["data"]
    phone = get_phone()["data"]
    list = [name,phone]
    return {"success": True, 
        "data": list, 
        "error" : None}


def get_choice():
    while True:
        try:
            choice = input("ADD / REMOVE / UPDATE / SEARCH / VIEW / EXIT:- ").lower()
        except KeyboardInterrupt:
            print()
            print("--Application Ended--")
            return {"success": False, 
                "data": None, 
                "error" : "user forced exit"}
        if choice in ["add","remove","update","delete","exit","duplicate","view"]:
            return {"success": True, 
                "data": choice, 
                "error" : None}

        print("-- Please enter among the following choices --")


def get_file():
    while True:
        file = input("get file name:- ")
        if valid.valid_file(file)["success"]:
            return {"success": True, 
                "data": file, 
                "error" : None}