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
        return {"success": False, "error": str(e)}


def write_csv(file, rows):
    result = read_csv(file)
    if result["success"] == True:
        crm = result["data"]
        header = result["header"]
        try:
            with open(file,"a",newline = '') as append_file:
                writer = csv.DictWriter(append_file, fieldnames=header)
                writer.writerow(rows)
                return {"success": True, "msg":"Row written to csv"}
        except (FileNotFoundError,PermissionError,UnicodeDecodeError) as e:
            return {"success" : False, "error" : e}
    return {"success" : False, "error" : "Error in reading file"}


def rewrite_csv(file,list_of_rows):
    result = read_csv(file)
    if result["success"] == True:
        # As write will anyway create a new file File not fpund error is excluded
        crm = result["data"]
        header = result["header"]
        with open(file, "w", newline='') as write_file:
            writer = csv.DictWriter(write_file, fieldnames=header)
            writer.writeheader()
            for row in list_of_rows:
                writer.writerow(row)
            return {"success" : True, "msg":"Csv rewritten"}
    return {"success" : False, "error" : "Error in reading file"}



def get_next_id(file):
    crm  = read_csv(file)[1]
    try:
        if crm != []:
            id_index = int(crm[-1]["ID"])
            return id_index + 1
        return "1"
    except IndexError:
        print("Index out of range")
        return None


def get_current_id(file, name, phone):
    crm = read_csv(file)[1]
    try:
        if crm != []:
            for row in crm:
                if row["Name"] == name and row["Phone"] == phone:
                    return row["ID"]
    except IndexError:
        print("Index out of range")
        return None


def find_row_by_id(file, user_id):
    crm = read_csv(file)[1]
    if str(user_id).isdigit():
        for row in crm:
            if row["ID"] == user_id:
                return 200, True, row
        return 200, False, None


def load_all(file):
    crm = read_csv(file)[1]
    header = read_csv(file)[2]
    if header != None:
        print(header)
    for row in crm:
        print(list(row.values()))


