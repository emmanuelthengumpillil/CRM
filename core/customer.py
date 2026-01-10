import storage
import valid
import inpt

f = "crm.csv"
row1 = {"Name": "hello", "Phone" : "1234567890"}
row2 = {"Phone" : "1234567890", "Name": "hello"}


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


def create_row_dict(file):
    keys = ["Id", "Name", "Phone"]
    if file["success"]:
        crm = file["data"]
        header = file["header"]
        keys = header
        if crm != []:
            name, phone = inpt.get_input()["data"]
            result_id = storage.get_current_id(file, name, phone)
            if result_id["success"]:
                if result_id["data"] != None:
                    values = [result_id["data"], name, phone]
                    row_dict = dict(zip(keys, values))
                if valid.validate_row(file, row_dict)["success"]:
                    return {"success": True, 
                        "data": row_dict, 
                        "error" : None}
                return {"success": False, 
                    "data": None, 
                    "error" : "Created row_dict invalid"}
            else:
                n_id = storage.get_next_id(file)
                if n_id != None:
                    if n_id != None:
                        values = [n_id["data"], name, phone]
                        row_dict = dict(zip(keys, values))
                    if valid.validate_row(file, row_dict)["success"]:
                        return {"success": True, 
                            "data": row_dict, 
                            "error" : None}
                    return {"success": False, 
                        "data": None, 
                        "error" : "Created row_dict invalid"}
        return {"success": False, 
            "data": None, 
            "error" : "Csv/Header is empty"}
    return {"success": False, 
        "data": None, 
        "error" : "Couldn't read csv"}


def add_person_crm(file, name, phone):
    row = create_row_dict(file)
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


def remove_person_crm(file):
    new_row = []
    if file["success"]:
        row_result = create_row_dict(file)
        if row_result["success"]:
            row_to_be_deleted = row_result["data"]
            for row in file["data"]:
                if row != row_to_be_deleted:
                    new_row.append(row)
            print(new_row)
            storage.rewrite_csv(file,file,new_row)
            return {"success": True, 
                "data": new_row, 
                "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "File not found"}


def create_duplicate_file(old_file, new_file):
    if old_file["success"]:
        write_result = storage.rewrite_csv(old_file,new_file)
        print(write_result)


def view_crm(file):
    x = storage.load_all(file)
    if x["success"]:
        for lt in x["data"]:
            print(lt)
            return {"success": True, 
                "data": "Successfully loaded crm", 
                "error" : None}
    else:
        return {"success": False, 
            "data": None, 
            "error" : "Couldn't read crm"}

