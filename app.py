import csv
import sys

def main():
    f = 'crm.csv'
    menu(f)

def menu(f):
    while True:
        try:
            n = input("Type ADD / REMOVE :- ").lower()
            add = ("a","add")
            remove = ("r", "remove")
            if n in add:
                print("ADD MENU:-")
                name = input("Enter name: ")
                phone = input("Enter Phone number: ")
                add_crm(name,phone,f)
            elif n in remove:
                print("REMOVE menu")
                name = input("Enter name: ")
                phone = input("Enter Phone number: ")
                remove_crm(name,phone,f)
            else:
                continue
        except KeyboardInterrupt:
            print("Session ended")
            sys.exit()
def add_crm(name,phone,f):
    with open(f, "a", newline='') as File:
        writer = csv.DictWriter(File, fieldnames=["Name","Phone"])
        # writer.writeheader()
        writer.writerow({"Name": name, "Phone": phone})
        print("added succesfully")
        return True

def remove_crm(name,phone,f):
    with open(f) as File:
        writer = csv.DictWriter(File)

if __name__ == "__main__":
    main()