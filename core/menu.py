import function
import inpt
import search
import sys

print("Welome to terminal crm")

ch = inpt.get_choice()
if ch["success"]:
    file = inpt.get_file()["data"]
else:
    sys.exit()

def menu(file):
    if ch["data"] == "add":
        add = function.add_person_crm(file)
        if add["success"]:
            print("Success")
        else:
            print(add["error"])
    elif ch["data"] == "search":
        srch = search.get_id_by_name(file)
        if srch["success"]:
            print("Success")
        else:
            print(srch["error"])
    elif ch["data"] == "remove":
        remove = function.remove_person_crm(file)
        if remove["success"]:
            print("Success")
        else:
            print(remove["error"])
    elif ch["data"] == "update":
        update = function.update_person_crm()
        if update["success"]:
            print("Success")
        else:
            print(update["error"])
    elif ch["data"] == "view":
        view = function.view_crm(file)
        if view["success"]:
            print("Success")
        else:
            print(view["error"])
    else:
        print("Choice not recognised")


if __name__ == "__main__":
    menu(file)