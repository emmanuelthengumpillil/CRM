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
            phone = row["Phone"]
            if row_list["Phone"] == phone:
                return {"success":False, "msg":"duplicate of list is found","location":"isduplicate"}
        return {"success":True, "data":row_list, "location":"isduplicate"}
    return {"success":False, "msg":"Couldn't read csv","location":"isduplicate"}


def create_row_dict(file):
    keys = ["Id", "Name", "Phone"]
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
                    return {"success":True, "data": row_dict, "location":"create_row_dict"}
                return {"success":False, "error": "Created row_dict invalid", "location":"create_row_dict"}
            else:
                n_id = storage.get_next_id(file)
                if n_id != None:
                    if n_id != None:
                        values = [n_id["data"], name, phone]
                        row_dict = dict(zip(keys, values))
                    if valid.validate_row(file, row_dict)["success"]:
                        return {"success":True, "data": row_dict, "crm":crm, "location":"create_row_dict"}
                    return {"success":False, "error": "Created row_dict invalid", "location":"create_row_dict"}
        return {"success":False, "error":"Csv/Header is empty", "location":"create_row_dict"}
    return {"success":False, "msg":"Couldn't read csv", "location":"create_row_dict"}


def add_person_crm(file):
    crm = storage.read_csv(file)
    row = create_row_dict(file)
    if row["success"]:
        data = row["data"]
        duplicate = is_duplicate(file,data)
        if duplicate["success"]:
            storage.write_csv(file, data)
            return {"success":True, "msg":"Successfully added person", "location":"add_person"}
        return {"success":True, "data":data, "location":"add_person"}
    return {"success":False, "error":"Couldn't add person", "location":"add_person"}


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
            return {"success":True, "data":new_row, "location":"remove_person"}
    return {"success": False, "error": "File not found", "location":"remove_person"}


def create_duplicate_file(old_file, new_file):
    old_result = storage.read_csv(old_file)
    if old_result["success"]:
        write_result = storage.rewrite_csv(old_file,new_file)
        print(write_result)


def search_person_crm():
    pass


def view_crm(file):
    x = storage.load_all(file)
    if x["success"]:
        for lt in x["data"]:
            print(lt)
            return {"success": True}
    else:
        return{"success": False}


def update_person_crm():
    pass


# view_crm("data//crm.csv")
