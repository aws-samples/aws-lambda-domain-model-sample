from datetime import datetime
'''
Slot: Domain Model
'''
class Slot:
    def __init__(self, slot_id:str, reservation_date:datetime, location:str):
        self.__slot_id = slot_id
        self.__reservation_date = reservation_date
        self.__location = location
        self.__is_vacant = True

    @property
    def slot_id(self):
        return self.__slot_id

    @property
    def reservation_date(self):
        return self.__reservation_date

    @property
    def location(self):
        return self.__location

    @property
    def is_vacant(self):
        return self.__is_vacant

    def use_slot(self):
        self.__is_vacant = False
