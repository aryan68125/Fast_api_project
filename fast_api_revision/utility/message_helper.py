from enum import Enum
class CommonErrorMessage(Enum):
    # Error messages related to CommonResponse class
    STATUS_CODE_ERROR = "Status code required!"

class CommonSuccessMessages(Enum):
    # index route messages
    SUCCESS_MESSAGE = "Well , Hello there I am index route up and runing in fast-api."