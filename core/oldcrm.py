import csv
import sys


def main():
    f = 'crm.csv'
    menu(f)


def menu(f):
    # To simulate menu buttons via function
    add = ("a","add")
    remove = ("r", "remove")
    exit = ("end", "exit", "e")
    
    while True:
        try:
            #try to repeat unless interpreted by keyboard
            user_input = input("--===Type ADD / REMOVE / EXIT:- ").lower()

            #uses variable to put all the possible values of menu btn
            

            if user_input in exit: 
                print("======= Session ended ========")
                sys.exit()

            elif user_input in add:
                print("=====ADD MENU:-=====")
                name,phone = get_input()
                add_crm(name,phone,f)

            elif user_input in remove:
                print("=====REMOVE menu:-=====")
                name,phone = get_input()
                remove_crm(name,phone,f)

            else:
                print("Enter valid input")
                continue

        except KeyboardInterrupt:
            print("Session ended")
            sys.exit()


def get_input():
    name = input("Enter name: ")
    while True:
        phone = input("Enter Phone number: ")
        if phone.isnumeric() and len(phone) >= 10: 
            return name,phone


def add_crm(name,phone,f):
    #open the csv file to write the input
    if present(name,phone,f) == False:
        with open(f, "a", newline='') as writing_file:
            writer = csv.DictWriter(writing_file, fieldnames=["Name","Phone"])
            writer.writerow({"Name": name, "Phone": phone})
            print("-----Added succesfully-----")
            return True
    else:
        print("-----Name, Phone  already exists-----")


def present(name,phone,f):
    # Check if it exists in csv
    with open(f,'r') as read_file:
        reader = csv.DictReader(read_file)
        x = 0

        for row in reader:
            if name == row['Name'] and phone == row['Phone']:
                x += 1

                if x > 0:
                    return True
                else:
                    return False


def remove_crm(name,phone,f):
    #To back_up_crm
    back_up_crm(f,"backup.csv")
    # TO read files into temp list
    temp = []
    with open(f,"r", newline='') as read_file:
        reader = csv.DictReader(read_file)
        for row in reader:
            temp.append(row)
    # To write without the specific row
    with open(f,"w", newline='') as write_file:
        writer = csv.DictWriter(write_file,fieldnames=["Name","Phone"])
        writer.writeheader()
        for row in temp:
            if name != row["Name"] or row["Phone"] != phone:
                writer.writerow({"Name":row["Name"], "Phone": row["Phone"]})


def back_up_crm(old,new):
    with open(old,'r',newline='') as read_file:
        reader = csv.DictReader(read_file)
        header = reader.fieldnames

        with open(new,'w',newline='') as back_up:
            writer = csv.DictWriter(back_up, fieldnames=header)
            writer.writeheader()
            for row in reader:
                writer.writerow({header[0]:row[header[0]], header[1]:row[header[1]]})


if __name__ == "__main__":
    main()