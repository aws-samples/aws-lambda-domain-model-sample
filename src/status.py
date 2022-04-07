'''
Helper class for Status Code
'''
class Status:
    def __init__(self, status_code:int, message:str):
        self.__status_code = status_code
        self.__message = message

    @property
    def status_code(self)->int:
        return self.__status_code
    
    @property
    def message(self)->str:
        return self.__message
