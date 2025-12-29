import function
import input

ch = input.get_choice()["data"]
file = "data\\crm.csv"

if ch == "add":
    function.add_person_crm(file)
elif ch == "search":
    function.search_person_crm()
elif ch == "remove":
    function.remove_person_crm()
elif ch == "update":
    function.update_person_crm()
elif ch == "view":
    function.view_crm()
else:
    print("Choice not recognised")

