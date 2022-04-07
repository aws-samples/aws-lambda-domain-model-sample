from abc import ABCMeta, abstractmethod
from slot import Slot

'''
interface of Slot output port
'''
class ISlotOutputPort(metaclass=ABCMeta):

    @abstractmethod
    def get_slot_by_id(self, slot_id:str) -> Slot:
        raise NotImplementedError()
