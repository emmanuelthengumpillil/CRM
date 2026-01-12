import customer
import inpt
import search
import storage
import sys

print("Welome to terminal crm")

path_file = inpt.get_file()
if path_file["success"]:
    crm_file = storage.read_csv(path_file["data"])
else:
    print("Invlid File")

while True:
    ch = inpt.get_choice()
    if ch["success"] == False:
        sys.exit()

    if ch["data"] == "add":
        name = inpt.get_name()["data"]
        phone = inpt.get_phone()["data"]
        add = customer.add_person_crm(crm_file, name, phone)
        if add["success"]:
            print("Success")
        else:
            print(add["error"])
    elif ch["data"] == "search":
        srch = search.get_id_by_name(crm_file)
        if srch["success"]:
            print("Success")
        else:
            print(srch["error"])
    elif ch["data"] == "remove":
        remove = customer.remove_person_crm(crm_file)
        if remove["success"]:
            print("Success")
        else:
            print(remove["error"])
    elif ch["data"] == "update":
        update = customer.update_person_crm(crm_file)
        if update["success"]:
            print("Success")
        else:
            print(update["error"])
    elif ch["data"] == "view":
        view = customer.view_crm(crm_file)
        if view["success"]:
            print("Success")
        else:
            print(view["error"])
    elif ch["data"] == "exit":
        sys.exit()
    else:
        print("Choice not recognised")
        break

