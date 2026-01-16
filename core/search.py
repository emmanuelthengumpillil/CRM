# Contains functions for searching 

def find_row_by_name(data,user_name):
    if data["success"]:
        for i in range(len(data["data"])):
            if data["data"][i]["Name"] in user_name:
                return {"success": True, 
                    "data": data["data"][i]["Name"], 
                    "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "Name not found"}


def find_id_by_phone(data, phone):
    for i in range(len(data["data"])):
        if phone == data["data"][i]["Phone"]:
            return {"success": True, 
                "data": data["data"][i]["Id"], 
                "error" : None}
    else:
        return {"success": False, 
            "data": None, 
            "error" : "Phone no not found"}


def get_next_id(file):
    if file["success"] == True:
        crm = file["data"]
        try:
            if crm != []:
                max_id = int(crm[-1]["Id"])
                for i in range(len(crm)):
                    if max_id < int(crm[-i]["Id"]):
                            max_id = int(crm[-i]["Id"])
                return {"success": True, 
                    "data": max_id + 1, 
                    "error" : None}
            return {"success": True, 
                "data": 0, 
                "error" : None}
        except IndexError:
            raise IndexError("Index Error found")
    raise FileNotFoundError("File not found")


def get_current_id(file, name, phone: str):
    crm = file["data"]
    if crm != []:
        for row in crm:
            if row["Name"] == name and row["Phone"] == phone:
                return {"success": True, 
                    "data": row["Id"], 
                    "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : None}


def find_row_by_id(file, user_id):
    crm = file["data"]
    if str(user_id).isdigit():
        for row in crm:
            if row["Id"] == str(user_id):
                return {"success": True,
                    "data": row,
                    "error": None}
        else:
            return {"success": False,
                "data": "User_id not in crm",
                "error": None}
    raise ValueError ("invalid data type")

