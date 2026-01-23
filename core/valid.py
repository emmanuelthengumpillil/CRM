import os
import re


def valid_row_data(row_dict):
    if not isinstance(row_dict, dict):
        return {"success": False, 
            "data": None, 
            "error" : "row data invalid"}
    return {"success": True, 
        "data": "Row data valid", 
        "error" : None}


def validate_keys(header, row_dict):
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


def validate_row(header,row_dict):
    if valid_row_data(row_dict)["success"]:
        if validate_keys(header, row_dict)["success"]:
            if validate_not_empty(row_dict)["success"]:
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
        if (str(letter).isalpha() or str(letter).isspace()) == False:
            return {"success": False, 
                "data": None, 
                "error" : "Conatains invalid data type"}
    return {"success": True, 
        "data": name, 
        "error" : None}


def valid_phone(phone):
    if str(phone).isdigit() and str(phone) != "":
        if 10 <= len(str(phone)) <= 12:
            return {"success": True, 
                "data": str(phone), 
                "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "Phone number is not valid"}


def valid_email(email):
    if re.search(r"^[^0-9@\s]+@[^0-9@\s]+\.com$", email):
        return {"success": True, 
            "data": email, 
            "error" : None}
    else:
        return {"success": False, 
            "data": None, 
            "error" : "Invalid Email"}


def valid_file(file):
    if os.path.exists(file):
        return {"success": True, 
            "data": file, 
            "error" : None}
    else:
        return {"success": False, 
            "data": "File doesnot exist", 
            "error" : None}
