from abc import ABCMeta, abstractmethod
from status import Status

'''
interface of Recipient input port
'''
class IRecipientInputPort(metaclass=ABCMeta):

    @abstractmethod
    def make_reservation(self, recipient_id:str, slot_id:str) -> Status:
        raise NotImplementedError()

