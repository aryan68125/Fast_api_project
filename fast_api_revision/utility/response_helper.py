#import for sending in custom resonses
from fastapi import Response

# import for error and succes messages
from utility.message_helper import CommonErrorMessage
class CommonResponse:
    def __init__(self,status_code,message = "",error = "",data = {}):
        self.status_code = status_code
        self.message = message
        self.error = error
        self.data = data
    
    def validate_response(self):
        if not self.status_code:
            return {"status":False, "error":CommonErrorMessage['STATUS_CODE_ERROR'].value}
        return {"status":True}
    def send_response(self):
        return Response(status=self.status_code,error=self.error,message=self.message,data=self.data)
        