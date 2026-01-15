import customer
import inpt
import search
import storage
import sys

print("Welome to terminal crm")

path_file = inpt.get_file()
if path_file["success"] == False:    
    print("Invalid File")
    sys.exit()


while True:
    ch = inpt.get_choice()
    choice = ch["data"]
    if ch["success"]:

        if choice in ("add","a"):
            name_res = inpt.get_name()
            if not name_res["success"]:
                print(name_res["error"])
                sys.exit()
            phone_res = inpt.get_phone()
            if not phone_res["success"]:
                print(phone_res["error"])
                sys.exit()
            add = customer.add_person_crm(storage.read_csv(path_file["data"]), name_res["data"], phone_res["data"])
            if add["success"]:
                print("Success")
            else:
                print(add["error"])

        elif choice in ("remove","r"):
            name_res = inpt.get_name()
            if not name_res["success"]:
                print(name_res["error"])
                sys.exit()
            phone_res = inpt.get_phone()
            if not phone_res["success"]:
                print(phone_res["error"])
                sys.exit()
            remove = customer.remove_person_crm(storage.read_csv(path_file["data"]), path_file, name_res["data"], phone_res["data"])
            if remove["success"]:
                print("Success")
            else:
                print(remove["error"])

        elif choice in ("search","s"):
            name_res = inpt.get_name()
            srch = search.find_row_by_name(storage.read_csv(path_file["data"]), name_res["data"])
            if not name_res["success"]:
                print(name_res["error"])
                sys.exit()
            if srch["success"]:
                print("Success")
                print(srch["data"])
            else:
                print(srch["error"])

# To be completed
        elif choice in ("update","u"):
            update = customer.update_person_crm(storage.read_csv(path_file["data"]))
            if update["success"]:
                print("Success")
            else:
                print(update["error"])

        elif choice in ("view","v"):
            view = customer.view_crm(storage.read_csv(path_file["data"]))
            if view["success"]:
                print("Success")
            else:
                print(view["error"])

        elif choice in ("exit","e"):
            sys.exit()

        else:
            print("Choice not recognised")

    else:
        sys.exit()


