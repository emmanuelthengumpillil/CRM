import core.inpt as inpt
# import core.menu as menu
# import core.storage as storage
# import core.function as functions


file = inpt.get_file()["data"]

while True:    
    choice = inpt.get_choice()
    if choice == "add":
        name = inpt.get_name()
        phone = inpt.get_phone()
        function.add_person_crm(file, name, phone)