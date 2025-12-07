import storage
import valid
import input

f = "crm.csv"
row1 = {"Name": "hello", "Phone" : "1234567890"}
row2 = {"Phone" : "1234567890", "Name": "hello"}

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


