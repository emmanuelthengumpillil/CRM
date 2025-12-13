import storage
import valid
import input

f = "crm.csv"
row1 = {"Name": "hello", "Phone" : "1234567890"}
row2 = {"Phone" : "1234567890", "Name": "hello"}


def is_duplicate(file,row_list):
    result = storage.read_csv(file)
    if result["success"]:
        crm = result["data"]
        for row in crm:        
            name = row["Name"]
            phone = row["Phone"]
            if row_list["Phone"] == phone:
                return {"success":True, "msg":"duplicate of list is found"}
        return {"success":False, "data":row_list}
    return {"success":True, "msg":"Couldn't read csv"}


def create_row_dict(file):
    keys = ["ID", "Name", "Phone"]
    result = storage.read_csv(file)
    if result["success"]:
        crm = result["data"]
        header = result["header"]
        keys = header
        if crm != []:
            name, phone = input.get_input()["data"]
            result_id = storage.get_current_id(file, name, phone)
            if result_id["success"]:
                if result_id["data"] != None:
                    values = [result_id["data"], name, phone]
                    row_dict = dict(zip(keys, values))
                if valid.validate_row(file, row_dict)["success"]:
                    return {"success":True, "data": row_dict}
                return {"success":False, "error": "Created row_dict invalid"}
            else:
                n_id = storage.get_next_id(file)
                if n_id != None:
                    if n_id != None:
                        values = [n_id["data"], name, phone]
                        row_dict = dict(zip(keys, values))
                    if valid.validate_row(file, row_dict)["success"]:
                        return {"success":True, "data": row_dict, "crm":crm}
                    return {"success":False, "error": "Created row_dict invalid"}
        return {"success":False, "error":"Csv/Header is empty"}
    return {"success":False, "msg":"Couldn't read csv"}


def add_person_crm(file):
    row = create_row_dict(file)
    if row["success"]:
        data = row["data"]
        duplicate = is_duplicate(file,data)
        print(duplicate)
        if duplicate["success"] == False:
            storage.write_csv(file, data)
            return {"success":True, "msg":"Successfully added person"}
    return {"success":False, "error":"Couldn't add person"}


def remove_person_crm(file):
    new_row = []
    result = storage.read_csv(file)
    if result["success"]:
        row_result = create_row_dict(file)
        if row_result["success"]:
            row_to_be_deleted = row_result["data"]
            for row in result["data"]:
                if row != row_to_be_deleted:
                    new_row.append(row)
            # print(new_row)
            storage.rewrite_csv(file,file,new_row)
            return {"success":True, "data":new_row}
    return {"success": False, "error": "File not found"}


def create_duplicate_file(old_file, new_file):
    result = storage.read_csv(old_file)
    if result["success"]:
        crm = result["data"]
        write_result = storage.rewrite_csv(old_file,new_file,crm)
        print(write_result)

create_duplicate_file(f,"crmcopy.csv")