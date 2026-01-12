import storage
import inpt


def get_id_by_name(data,user_name):
    for i in range(len(data["data"])):
        if (data["data"][i]["Name"].lower()) == user_name:
            return {"success": True, 
                "data": data["data"][i]["Id"], 
                "error" : None}
        else:
            return {"success": False, 
                "data": None, 
                "error" : "Name not found"}



def get_id_by_phone(data, phone):
    for i in range(len(data["data"])):
        if phone == data["data"][i]["Phone"]:
            return {"success": True, 
                "data": data["data"][i]["Id"], 
                "error" : None}
        else:
            return {"success": False, 
                "data": None, 
                "error" : "Phone no not found"}
