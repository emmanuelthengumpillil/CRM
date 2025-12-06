import csv

f  = 'crm.csv'
l = {'Name': 'hello', 'Phone' : '123456890'}

def read_csv(file):
    crm_list = []
    try:
        with open(file,'r',newline='') as reading_file:
            reader = csv.DictReader(reading_file)
            header = reader.fieldnames
            if header != None:
                for row in reader:
                    crm_list.append(row)
            return 200, crm_list, header
    except FileNotFoundError:
        return 404, None, None


def write_csv(file, rows):
    crm = read_csv(file)[1]
    header = read_csv(file)[2]
    try:
        with open(file,"a",newline = '') as append_file:
            writer = csv.DictWriter(append_file, fieldnames=header)
            writer.writerow(rows)
            return 200, crm, None
    except FileNotFoundError:
        return 404, None, None


def rewrite_csv(file,list_of_rows):
    crm = read_csv(file)[1]
    header = read_csv(file)[2]
    # As write will anyway create a new file File not fpund error is excluded
    with open(file, "w", newline='') as write_file:
        writer = csv.DictWriter(write_file, fieldnames=header)
        writer.writeheader()
        for row in crm:
            writer.writerow(row)
        return 200, list_of_rows, None


def get_next_id(file):
    crm  = read_csv(file)[1]
    id_index = int(crm[-1]["ID"])
    return id_index + 1

