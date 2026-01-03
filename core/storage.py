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
        raise FileNotFoundError("File not found")


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


def rewrite_csv(old_file,new_file, new_row):
    old_result = read_csv(old_file)
    if old_result["success"] == True:
        old_crm = old_result["data"]
        old_header = old_result["header"]
        with open(new_file, "w", newline='') as write_file:
            writer = csv.DictWriter(write_file, fieldnames=old_header)
            writer.writeheader()
            for row in new_row:
                writer.writerow(row)
            return {"success" : True, "msg":"Csv rewritten"}
    return {"success" : False, "error" : "Error in reading file"}


def get_next_id(file):
    result = read_csv(file)
    if result["success"] == True:
        crm = result["data"]
        try:
            if crm != []:
                id_index = int(crm[-1]["Id"])
                return {"success":True, "data": id_index + 1, "crm" : result}
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
                        return {"success":True, "data": row["Id"], "crm" : result}
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
                if row["Id"] == user_id:
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
        return {"success":True,"data":copy, "crm" : result}
    return {"success" : False, "error" : "Error in reading file"}


#sort_crm not working
def sort_crm(file, new_file):
    crm = read_csv(file)
    if crm["success"]:
        sort = []
        for row1 in crm["data"]:
            r1 = row1["Name"]
            for row2 in crm["data"]:
                r2 = row2["Name"]
                if r1 > r2:
                    r1, r2 = r2, r1
            sort.append(r1)
        print(sort)
        # rewrite_csv(file, new_file)
        return {"success": True, "data":sort}


def get_id(file,name):
    pass


# sort_crm("data\\crm.csv", "data\\sorted_crm.csv")