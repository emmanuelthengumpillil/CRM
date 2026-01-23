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


def rewrite_csv(old_header, new_file, new_row):
    with open(new_file, "w", newline='') as write_file:
        writer = csv.DictWriter(write_file, fieldnames=old_header)
        writer.writeheader()
        for row in new_row:
            writer.writerow(row)
        return {"success": True, 
            "data": "Crm rewritten", 
            "error" : None}



def duplicate_csv(old_file,new_file):
    old_header = old_file["header"]
    with open(new_file, "w", newline="") as write_file:
        writer = csv.DictWriter(write_file, fieldnames = old_header)
        writer.writeheader()
        for i in old_file["data"]:
            writer.writerow(i)

