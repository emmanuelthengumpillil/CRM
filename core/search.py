import storage
import inpt

def bubble_sort_name(data):
    if data["success"]:
        l = len(data["data"])
        for i in range(l):
            for j in range(0,l-i-1):
                if data["data"][j]["Name"] > data["data"][j+1]["Name"]:
                    data["data"][j], data["data"][j + 1] = data["data"][j + 1], data["data"][j]
        return{"success":True, "data": data["data"]}
    return {"success": False, "data": None}


def get_id_by_name(data):
    user_name = inpt.get_name()
    if data["success"]:
        sorted_data = bubble_sort_name(data)["data"]
        for i in range(len(sorted_data)):
            if user_name == sorted_data[i]["Name"].lower():
                return {"success": True, "data": sorted_data[i]["Id"]}
        return {"success": False, "error": "--Name not found--"}
    return {"success": False, "error": "Couldn't get user_id"}


def get_id_by_phone(data):
    phone = inpt.get_phone()
    if data["success"]:
        for i in range(len(data["data"])):
            if phone == data["data"][i]["Phone"]:
                return {"success": True, "data": data["data"][i]["Id"]}
        return {"success": False, "error" :"Phone no not found"}
    return {"success": False, "error": "Couldn't read crm"}


