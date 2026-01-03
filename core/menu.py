import function
import inpt
import search


print("Welome to terminal crm")
ch = inpt.get_choice()["data"]
file = inpt.get_file()["data"]


def menu(file):
    if ch == "add":
        add = function.add_person_crm(file)
        if add["success"]:
            print("Success")
        else:
            print(add["error"])
    elif ch == "search":
        search = search.get_id_by_name(file)
        if search["success"]:
            print("Success")
        else:
            print(search["error"])
    elif ch == "remove":
        remove = function.remove_person_crm(file)
        if remove["success"]:
            print("Success")
        else:
            print(remove["error"])
    elif ch == "update":
        update = function.update_person_crm()
        if update["success"]:
            print("Success")
        else:
            print(update["error"])
    elif ch == "view":
        view = function.view_crm(file)
        if view["success"]:
            print("Success")
        else:
            print(view["error"])
    else:
        print("Choice not recognised")


if __name__ == "__main__":
    menu(file)