import csv


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
    except (FileNotFoundError) as e:
        raise FileNotFoundError(e)
    except (PermissionError) as e:
        raise PermissionError(e)
    except (UnicodeEncodeError) as e:
        raise UnicodeEncodeError(e)

def write_csv(file, rows):
    if file["success"] == True:
        header = file["header"]
        try:
            with open(file,"a",newline = '') as append_file:
                writer = csv.DictWriter(append_file, fieldnames=header)
                writer.writerow(rows)
                return {"success": True, "msg":"Row written to csv"}
        except (FileNotFoundError) as e:
            raise FileNotFoundError(e)
        except (PermissionError) as e:
            raise PermissionError(e)
        except (UnicodeEncodeError) as e:
            raise UnicodeEncodeError(e)
    raise FileNotFoundError("File not found")


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
    raise FileNotFoundError("File not found")


def get_next_id(file):
    if file["success"] == True:
        crm = file["data"]
        try:
            if crm != []:
                sorted_crm = sorted(crm["Id"])
                id_index = int(sorted_crm[-1]["Id"])
                return {"success":True, "data": id_index + 1, "crm" : file}
            return {"success":False, "error": "Csv is empty"}
        except IndexError:
            raise IndexError("Index Error found")
    raise FileNotFoundError("File not found")


def get_current_id(file, name, phone):
    if file["success"] == True:
        crm = file["data"]
        try:
            if crm != []:
                for row in crm:
                    if row["Name"] == name and row["Phone"] == phone:
                        return {"success":True, "data": row["Id"], "crm" : file}
            return {"success":False, "error": "Csv is empty"}
        except IndexError:
            raise IndexError("Index Error found")
    raise FileNotFoundError("File not found")


def find_row_by_id(file, user_id):
    if file["success"] == True:
        crm = file["data"]
        if str(user_id).isdigit():
            for row in crm:
                if row["Id"] == user_id:
                    return {"success":True, "data": row}
        raise ValueError ("invalid data type")
    raise FileNotFoundError("File not found")


def load_all(file):
    copy = []
    if file["success"] == True:
        crm = file["data"]
        header = file["header"]
        if header != None:
            copy.append(header)
        for row in crm:
            row_list = list(row.values())
            copy.append(row_list)
        return {"success":True,"data":copy, "crm" : file}
    raise FileNotFoundError("File not found")


#sort_crm not working
def sort_crm(file, new_file):
    crm = file
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
    raise FileNotFoundError("File not found")

