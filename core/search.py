import storage

user_list = [7,1,3,4,5,3,5,6,8,9,4,7,6,8,6,5,4,5,7,8,9,8,9,0,7]

def bubble_sort(dit):
    data = storage.read_csv(dit)
    if data["success"]:
        l = len(data["data"])
        for i in range(l):
            for j in range(0,l-i-1):
                if data["data"][j]["Name"] > data["data"][j+1]["Name"]:
                    data["data"][j], data["data"][j + 1] = data["data"][j + 1], data["data"][j]
        return{"success":True, "data": data["data"]}
    return {"success": False, "data": None}


def search(user_name):
    pass