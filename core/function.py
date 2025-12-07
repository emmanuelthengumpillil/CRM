import storage
import valid
import input

f = "crm.csv"
row1 = {"Name": "hello", "Phone" : "1234567890"}
row2 = {"Phone" : "1234567890", "Name": "hello"}

def is_duplicate(file):
    name = input.get_name()[2]
    phone = input.get_phone()[2]
    crm = storage.read_csv(file)[1]
    for row in crm:
        if row["Name"] == name or row["Phone"] == phone:
            return 200, True
    return 404, False


def create_row_dict(file):
    keys = ["ID", "Name", "Phone"]
    id = storage.get_next_id(file)
    if id != None:
        values = [id, input.get_name()[2], input.get_phone()[2]]
    row_dict = dict(zip(keys, values))
    if valid.validate_row(file, row_dict):
        return 200, row_dict
    return 400, None


def add_person_crm(file):
    crm = storage.read_csv(file)[1]
    row = create_row_dict(f)[1]
    if row != None:
        if valid.validate_row(file, row)[1]:
            storage.write_csv(file, row)
            return 200, crm, True
    return 404, crm, False


def remove_person_crm(file):
    new_row = []
    crm = storage.read_csv(file)[1]
    old_row = create_row_dict(f)[1]
    if valid.validate_row(file, old_row)[1] == True:
        read_file = storage.read_csv(file)[1]
        for row in read_file:
            if row != old_row:
                new_row.append(row)
        # print(new_row)
        storage.write_csv(file,new_row)
        return 202, crm, None
    return 404, crm, None 


# print(remove_person_crm(f,row1))
print(is_duplicate(f))