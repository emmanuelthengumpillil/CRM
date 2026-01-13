import customer
import inpt
import search
import storage
import sys

print("Welome to terminal crm")

# path_file = inpt.get_file()
# if path_file["success"]:
crm_file = "data\\crm.csv"
# else:
    # print("Invlid File")

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
            add = customer.add_person_crm(storage.read_csv(crm_file), name_res["data"], phone_res["data"])
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
            remove = customer.remove_person_crm(storage.read_csv(crm_file), crm_file, name_res["data"], phone_res["data"])
            if remove["success"]:
                print("Success")
            else:
                print(remove["error"])

        elif choice in ("search","s"):
            srch = search.get_id_by_name(crm_file)
            if srch["success"]:
                print("Success")
            else:
                print(srch["error"])

        elif choice in ("update","u"):
            update = customer.update_person_crm(crm_file)
            if update["success"]:
                print("Success")
            else:
                print(update["error"])

        elif choice in ("view","v"):
            view = customer.view_crm(crm_file)
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


