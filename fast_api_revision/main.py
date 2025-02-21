from fastapi import FastAPI, status

# for sending in custom response
from utility.response_helper import CommonResponse

# for common error and success messages
from utility.message_helper import CommonErrorMessage, CommonSuccessMessages
#instance of fast api
app = FastAPI()

@app.get('/')
def index():
    return CommonResponse(status_code=status.HTTP_200_OK,message=CommonSuccessMessages['SUCCESS_MESSAGE'].value)