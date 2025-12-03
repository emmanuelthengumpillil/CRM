import csv

f  = 'crm.csv'
l = {'Name': 'hello', 'Phone' : '123456890'}

def read_csv(file):
    crm_list = []
    try:
        with open(file,'r',newline='') as reading_file:
            reader = csv.DictReader(reading_file)
            header = reader.fieldnames
            for row in reader:
                crm_list.append(row)
            return 200, crm_list, header
    except FileNotFoundError:
        return 404, None, None

def append_csv(file, row_dict):
    try:
        header = read_csv(file)[2]
        with open(file,"a",newline = '') as append_file:
            writer = csv.DictWriter(append_file, fieldnames=header)
            writer.writerow(row_dict)
            return 200
    except FileNotFoundError:
        return 404
    except TypeError:
        return 400
