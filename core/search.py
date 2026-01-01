import storage

user_list = [7,1,3,4,5,3,5,6,8,9,4,7,6,8,6,5,4,5,7,8,9,8,9,0,7]
zero = list.count(0)
one = list.count(1)
two = list.count(2)
three = list.count(3)
four = list.count(4)
five = list.count(5)
six = list.count(6)
seven = list.count(7)
eight = list.count(8)
nine = list.count(9)

# How many letters are there
# print(f"Zero: {zero}, One: {one}, Three: {three}, Four: {four}, Five: {five}, six: {six}, seven: {seven}, eight: {eight}, nine: {nine}")

def bubble_sort(user_list):
    lst = user_list
    l = len(lst)
    for i in range(l):
        for j in range(0,l-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return{"success":True, "data": lst}

print(bubble_sort(list)["data"])
