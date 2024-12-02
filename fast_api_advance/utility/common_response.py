def response(status,error="",message="",data={}):
    if error is None:
        error=""
    if message is None:
        message=""
    if data is None:
        data={}
    return {"status":status, "error":error,"message":message,"data":data}