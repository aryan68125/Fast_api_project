def common_response(status_code,message="",error="",data={}):
    return {"status":status_code,"message":message,"error":error,"data":data}