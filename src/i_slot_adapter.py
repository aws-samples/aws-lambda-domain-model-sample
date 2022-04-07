from abc import ABCMeta, abstractmethod
from slot import Slot

'''
interface of Slot adapter
'''
class ISlotAdapter(metaclass=ABCMeta):
    
    @abstractmethod
    def load(self, slot_id:str) -> Slot:
        raise NotImplementedError()
