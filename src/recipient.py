from slot import Slot

'''
Recipient: Domain Model
'''
class Recipient:
    def __init__(self, recipient_id:str, email:str, first_name:str, last_name:str, age:int):
        self.__recipient_id = recipient_id
        self.__email = email
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__slots = []

    @property
    def recipient_id(self):
        return self.__recipient_id
    
    @property
    def email(self):
        return self.__email

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    @property
    def slots(self):
        return self.__slots

    def are_slots_same_date(self, slot:Slot) -> bool:
        for selfslot in self.__slots:
            if selfslot.reservation_date == slot.reservation_date:
                return True        
        return False

    def is_slot_counts_equal_or_over_two(self) -> bool:
        if len(self.__slots) >= 2:
            return True
        return False
    
    def add_reserve_slot(self, slot:Slot) -> bool:        
        if self.are_slots_same_date(slot):
            return False

        if self.is_slot_counts_equal_or_over_two():
            return False
        
        self.__slots.append(slot)
        slot.use_slot()
        return True
