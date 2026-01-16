import storage
import valid
import search


def is_duplicate(file,row_list):
    if file["success"]:
        crm = file["data"]
        for row in crm:
            phone = row["Phone"]
            if row_list["Phone"] == phone:
                return {"success": False, 
                    "data": None, 
                    "error" : "duplicate of list is found"}
        return {"success": True, 
            "data": row_list, 
            "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "Couldn't read csv"}


def create_row_dict(file, name, phone):
    if file["success"]:
        if file["data"] != []:
            header = file["header"] 
            result_id = search.get_current_id(file, name, phone)
            if result_id["success"]:
                values = [result_id["data"], name, phone]
                row_dict = dict(zip(header, values))
                if valid.validate_row(file, row_dict)["success"]:
                    return {"success": True, 
                        "data": row_dict, 
                        "error" : None}
                return {"success": False, 
                    "data": None, 
                    "error" : "Created row_dict invalid"}
            else:
                next_id = search.get_next_id(file)
                values = [next_id["data"], name, phone]
                row_dict = dict(zip(header, values))
                if valid.validate_row(file, row_dict)["success"]:
                    return {"success": True, 
                        "data": row_dict, 
                        "error" : None}
                return {"success": False, 
                    "data": None, 
                    "error" : "Created row_dict invalid"}
        return {"success": False, 
            "data": None, 
            "error" : "Csv is empty"}
    return {"success": False, 
            "data": None, 
            "error" : "Couldn,t read file"}


def add_person_crm(file, name, phone):
    row = create_row_dict(file, name, phone)
    if row["success"]:
        data = row["data"]
        duplicate = is_duplicate(file,data)
        if duplicate["success"]:
            storage.write_csv(file, data)
            return {"success": True, 
                "data": "Successfully added person", 
                "error" : None}
        return {"success": True, 
            "data": data, 
            "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "Couldn't add person"}


def remove_person_crm(old_file, new_file, name, phone):
    new_row = []
    if old_file["success"]:
        row_result = create_row_dict(old_file, name, phone)
        if row_result["success"]:
            for row in old_file["data"]:
                if row["Name"] != row_result["data"]["Name"]:
                    new_row.append(row)
        storage.rewrite_csv(old_file, new_file, new_row)
        return {"success": True, 
            "data": new_row, 
            "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "File not found"}


def create_duplicate_file(old_file, new_file):
    if old_file["success"]:
        crm_copy = old_file["data"]
        write_result = storage.rewrite_csv(old_file,new_file, crm_copy)
        if write_result["success"]:
            return {"success": True,
                "data": write_result,
                "error": None}
        return {"success": False,
            "data": None,
            "error": "Couldn't rewrite crm"}
    return {"success": False,
        "data": None,
        "error": "Couldn't read old_file"}


def view_crm(file):
    if file["success"]:
        for lst in file["data"]:
            print(lst)
        return {"success": True, 
            "data": "Successfully loaded crm", 
            "error" : None}
    else:
        return {"success": False, 
            "data": None, 
            "error" : "Couldn't read crm"}


def update_person_crm(file, old_name, new_name, phone):
    file_name = file["file_name"]
    if file["success"]:
        search_name = search.find_row_by_name(file, old_name)
        if search_name["success"]:
            phno = search_name["data"]["Phone"]
            rem = remove_person_crm(file, file_name, old_name, phno)
            add = add_person_crm(file, new_name, phno)
            if add["success"]:
                return{"success": True,
                    "data": add["data"],
                    "error": None} 
            return{"success": False,
                "data": None,
                "error": "Couldn't add person"}
        else:
            add = add_person_crm(file, new_name, phone)
            if add["success"]:
                return{"success": True,
                    "data": add["data"],
                    "error": None} 
        return{"success": False,
            "data": None,
            "error": None} 
    return{"success": False,
        "data": None,
        "error": None}
