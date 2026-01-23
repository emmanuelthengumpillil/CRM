# Contains functions for searching 

def find_row_by_name(data,user_name):
    for i in range(len(data)):
        if data[i]["Name"] in user_name:
            return {"success": True, 
                "data": data[i]["Name"], 
                "error" : None}

def find_id_by_phone(data, phone):
    for i in range(len()):
        if phone == data[i]["Phone"]:
            return {"success": True, 
                "data": data[i]["Id"], 
                "error" : None}
    else:
        return {"success": False, 
            "data": None, 
            "error" : "Phone no not found"}


def get_next_id(file):
    try:
        if file != []:
            max_id = int(file[-1]["Id"])
            for i in range(len(file)):
                if max_id < int(file[-i]["Id"]):
                        max_id = int(file[-i]["Id"])
            return {"success": True, 
                "data": max_id + 1, 
                "error" : None}
        return {"success": True, 
            "data": 0, 
            "error" : None}
    except IndexError:
        raise IndexError("Index Error found")



def get_current_id(file, name, phone: str):
    if file != []:
        for row in file:
            if row["Name"] == name and row["Phone"] == phone:
                return {"success": True, 
                    "data": row["Id"], 
                    "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : None}


def find_row_by_id(file, user_id):
    if str(user_id).isdigit():
        for row in file:
            if row["Id"] == str(user_id):
                return {"success": True,
                    "data": row,
                    "error": None}
        else:
            return {"success": False,
                "data": "User_id not in crm",
                "error": None}
    raise ValueError ("invalid data type")

