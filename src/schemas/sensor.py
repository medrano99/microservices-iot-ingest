
def sensorEntity(item)->dict:
    return {
        "id":str(item["_id"]),
        "id_device": item["id_device"],
        "temperature":item["temperature"],
        "timestamp":item["timestamp"]

    }

def sensorsEntity(entity)->list:
    return [ sensorEntity(item) for item in entity ]