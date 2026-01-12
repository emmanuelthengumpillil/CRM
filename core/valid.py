import re
import os

row = {"Name":"jkljk","Phone":"13213"}
row2 = {"Phone":"132465","Name":"qweqw"}
f = "crm.csv"


def valid_row_data(row_dict):
    if not isinstance(row_dict, dict):
        return {"success": False, 
            "data": None, 
            "error" : "row data invalid"}
    return {"success": True, 
        "data": "Row data valid", 
        "error" : None}


def validate_keys(file, row_dict):
    header = file[1]
    if header == None:
        return {"success": False, 
            "data": None, 
            "error" : "Header is empty"}
    if set(header) != set(row_dict.keys()):
        return {"success": False, 
            "data": None, 
            "error" : "Keys invalid"}
    return {"success": True, 
        "data": "Keys are valid", 
        "error" : None}


def validate_not_empty(row_dict):
    for i in row_dict.values():
        if i == "" or i == None:
            return {"success": False, 
                "data": None, 
                "error" : "Row is empty"}
    return {"success": True, 
        "data": "Row not empty", 
        "error" : None}


def validate_row(file,row_dict):
    if valid_row_data(row_dict):
        if validate_keys(file, row_dict):
            if validate_not_empty(row_dict):
                return {"success": True, 
                    "data": row_dict, 
                    "error" : None}
            return {"success": False, 
                "data": None, 
                "error" : "row_dict is empty"}
        return {"success": False, 
            "data": None, 
            "error" : "Key is not valid"}
    return {"success": False, 
        "data": None, 
        "error" : "Row_data invalid"}


def valid_name(name):
    if name == "":
        return {"success": False, 
            "data": None, 
            "error" : "Name is empty"}
    for letter in name:
        if not (str(letter).isalpha() or str(letter).isspace()):
            return {"success": False, 
                "data": None, 
                "error" : "Conatains invalid data type"}
    return {"success": True, 
        "data": name, 
        "error" : None}


def valid_phone(phone):
    if str(phone).isdigit() and phone != "":
        if 10 <= len(phone) <= 12:
            return {"success": True, 
                "data": phone, 
                "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "Phone number is not valid"}


def valid_file(file):
    while True:
        if os.path.exists(file):
            return {"success": True, 
                "data": "File exist", 
                "error" : None}
        else:
            return {"success": False, 
                "data": "File doesnot exist", 
                "error" : None}