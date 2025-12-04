import valid

def get_name():
    while True:
        name = input("Enter Name:- ")
        if name.isalpha():
            return name, 200

def get_phone():
    while True:
        try:
            phone = input("Enter Phone:- ")
            if phone.isnumeric and 10 <= (len(phone)) <= 12:
                return phone, 200
        except ValueError:
            return None, 404

