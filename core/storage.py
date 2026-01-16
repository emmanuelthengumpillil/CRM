import csv


def read_csv(file):
    crm_list = []
    try:
        with open(file,'r',newline='') as reading_file:
            reader = csv.DictReader(reading_file)
            header = reader.fieldnames
            if header == None or header == "" or header == []:
                return {"success": False, 
                    "data" : "Header is missing", 
                    "file_name" : file,
                    "error" : "File is empty"}
            for row in reader:
                crm_list.append(row)
            return {"success": True, 
                "data": crm_list,
                "header": header,
                "file_name" : file,
                "error" : None}
    except (FileNotFoundError) as e:
        raise FileNotFoundError(e)
    except (PermissionError) as e:
        raise PermissionError(e)
    except (UnicodeEncodeError) as e:
        raise UnicodeEncodeError(e)


def write_csv(file, row):
    header = file["header"]
    file_name = file["file_name"]
    try:
        with open(file_name,"a",newline = '') as append_file:
            writer = csv.DictWriter(append_file, fieldnames=header)
            writer.writerow(row)
            return {"success": True, 
                "data": "Succesfully written crm", 
                "error" : None}
    except (FileNotFoundError) as e:
        raise FileNotFoundError(e)
    except (PermissionError) as e:
        raise PermissionError(e)
    except (UnicodeEncodeError) as e:
        raise UnicodeEncodeError(e)


def rewrite_csv(old_file, new_file, new_row):
    if old_file["data"] != []:
        header = old_file["header"]
        with open(new_file, "w", newline='') as write_file:
            writer = csv.DictWriter(write_file, fieldnames=header)
            writer.writeheader()
            for row in new_row:
                writer.writerow(row)
            return {"success": True, 
                "data": "Crm rewritten", 
                "error" : None}
    return {"success": False, 
        "data": None, 
        "error" : "old_file is empty"}


def duplicate_csv(old_file,new_file):
    old_header = old_file["header"]
    with open(new_file, "w", newline="") as write_file:
        writer = csv.DictWriter(write_file, fieldnames = old_header)
        writer.writeheader()
        for i in old_file["data"]:
            writer.writerow(i)


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


def get_current_id(file, name, phone):
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
            if crm["Id"] == user_id:
                return {"success": True,
                    "data": row,
                    "error": None}
            else:
                return {"success": False,
                    "data": "User_id not in crm",
                    "error": None}
    raise ValueError ("invalid data type")


