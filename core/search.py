import storage
import inpt


def find_row_by_name(data,user_name):
    if data["success"]:
        for i in data["data"]:
            # USE PRINT TO CHECK THE TYPE OF SORT
            # print(i)
            if i["Name"] in user_name:
                return {"success": True, 
                    "data": i, 
                    "error" : None}
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
