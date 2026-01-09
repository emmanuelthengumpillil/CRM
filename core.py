import core.inpt as inpt



file = inpt.get_file()["data"]

while True:    
    choice = inpt.get_choice()
    if choice == "add":
        name = inpt.get_name()
        phone = inpt.get_phone()
        function.add_person_crm(file, name, phone)