import csv

f  = 'crm.csv'
x = {'Name': 'hello', 'Phone' : '123456890'}
l = [{'Name': 'hello', 'Phone' : '123456890'}]

def read_csv(file):
    crm_list = []
    try:
        with open(file,'r',newline='') as reading_file:
            reader = csv.DictReader(reading_file)
            header = reader.fieldnames
            if header == None or header == "" or header == []:
                return {"success": False, "data":"Couldn't read","error": "File is empty, Header is None"}
            for row in reader:
                crm_list.append(row)
            return {"success": True, "data": crm_list, "header" : header}
    except (FileNotFoundError,PermissionError,UnicodeDecodeError) as e:
        return {"success": False, "error": "File not found"}


def write_csv(file, rows):
    result = read_csv(file)
    if result["success"] == True:
        header = result["header"]
        try:
            with open(file,"a",newline = '') as append_file:
                writer = csv.DictWriter(append_file, fieldnames=header)
                writer.writerow(rows)
                return {"success": True, "msg":"Row written to csv"}
        except (FileNotFoundError,PermissionError,UnicodeDecodeError) as e:
            return {"success" : False, "error" : e}
    return {"success" : False, "error" : "Error in reading file"}


def rewrite_csv(file,new_file,list_of_rows):
    result = read_csv(file)
    if result["success"] == True:
        # As write will anyway create a new file File not fpund error is excluded
        crm = result["data"]
        header = result["header"]
        with open(new_file, "w", newline='') as write_file:
            writer = csv.DictWriter(write_file, fieldnames=header)
            writer.writeheader()
            for row in list_of_rows:
                writer.writerow(row)
            return {"success" : True, "msg":"Csv rewritten"}
    return {"success" : False, "error" : "Error in reading file"}



def get_next_id(file):
    result = read_csv(file)
    if result["success"] == True:
        crm = result["data"]
        try:
            if crm != []:
                id_index = int(crm[-1]["id"])
                return {"success":True, "data": id_index + 1}
            return {"success":False, "error": "Csv is empty"}
        except IndexError:
            return {"success":False, "error": "Index out of range"}
    return {"success" : False, "error" : "Error in reading file"}


def get_current_id(file, name, phone):
    result = read_csv(file)
    if result["success"] == True:
        crm = result["data"]
        try:
            if crm != []:
                for row in crm:
                    if row["Name"] == name and row["Phone"] == phone:
                        return {"success":True, "data": row["id"]}
            return {"success":False, "error": "Csv is empty"}
        except IndexError:
            return {"success":False, "error": "Index out of range"}
    return {"success" : False, "error" : "Error in reading file"}


def find_row_by_id(file, user_id):
    result = read_csv(file)
    if result["success"] == True:
        crm = result["data"]
        if str(user_id).isdigit():
            for row in crm:
                if row["ID"] == user_id:
                    return {"success":True, "data": row}
        return {"success":False, "error": "user_id not integer"}
    return {"success" : False, "error" : "Error in reading file"}


def load_all(file):
    result = read_csv(file)
    copy = []
    if result["success"] == True:
        crm = result["data"]
        header = result["header"]
        if header != None:
            copy.append(header)
        for row in crm:
            row_list = list(row.values())
            copy.append(row_list)
        return {"success":True,"data":copy}
    return {"success" : False, "error" : "Error in reading file"}

