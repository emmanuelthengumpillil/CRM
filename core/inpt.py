import valid
import sys

def get_name():
    while True:
        try:
            name = input("Enter Name:- ")
            if valid.valid_name(name)["success"]:
                return {"success": True, 
                    "data": name, 
                    "error" : None}
        except KeyboardInterrupt:
            return {"success": False, 
                "data": None, 
                "error" : "\nGet name gone wrong"}


def get_phone():
    while True:
        try:
            phone = input("Enter Phone:- ")
            if valid.valid_phone(phone)["success"]:
                return {"success": True, 
                    "data": phone, 
                    "error" : None}
        except KeyboardInterrupt:
            return {"success": False, 
                "data": None, 
                "error" : "\nGet phone gone wrong"}

def get_id():
    while True:
        try:
            id = input("Enter ID:- ")
            if id.isdigit():
                return {"success": True, 
                    "data": id, 
                    "error" : None}
        except KeyboardInterrupt:
            return {"success": False, 
                "data": None, 
                "error" : "\nGet id gone wrong"}


def get_input():
    name = get_name()["data"]
    phone = get_phone()["data"]
    if name["success"] == True and phone["success"] == True:
        list = [name,phone]
        return {"success": True, 
            "data": list, 
            "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "Get name gone wrong"}


def get_choice():
    while True:
        try:
            choice = input("ADD / REMOVE / UPDATE / SEARCH / VIEW / EXIT:- ").lower().strip()
        except KeyboardInterrupt:
            print()
            print("--Application Ended--")
            return {"success": False, 
                "data": None, 
                "error" : "user forced exit"}
        if choice in ["add","remove","update","delete","duplicate","view","a","r","u","d","v","e","q"]:
            return {"success": True, 
                "data": choice, 
                "error" : None}
        elif choice == "exit":
            sys.exit()
        else:
            print("-- Please enter among the following choices --")


def get_file():
    while True:
        try:
            file = input("get file name:- ")
            if valid.valid_file(file)["success"]:
                return {"success": True, 
                    "data": file, 
                    "error" : None}
        except KeyboardInterrupt:
            return {"success": False, 
                "data": None, 
                "error" : "get_file gone wrong"}