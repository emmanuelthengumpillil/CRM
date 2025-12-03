import csv

f  = 'crm.csv'

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

print(read_csv(f))
