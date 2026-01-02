import storage


def bubble_sort(data):
    if data["success"]:
        l = len(data["data"])
        for i in range(l):
            for j in range(0,l-i-1):
                if data["data"][j]["Name"] > data["data"][j+1]["Name"]:
                    data["data"][j], data["data"][j + 1] = data["data"][j + 1], data["data"][j]
        return{"success":True, "data": data["data"]}
    return {"success": False, "data": None}


def get_id_by_name(user_name, crm):
    user_name = user_name.lower()
    data = storage.read_csv(crm)
    if data["success"]:
        sorted_data = bubble_sort(data)["data"]
        for i in range(len(sorted_data)-1):
            if user_name == sorted_data[i]["Name"]:
                return {"success": True, "data": sorted_data[i]["Id"]}
        return {"success": False, "error": "--Name not found--"}
    return {"success": False, "error": "Couldn't get user_id"}

