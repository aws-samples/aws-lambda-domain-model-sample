from abc import ABCMeta, abstractmethod
from recipient import Recipient

'''
interface of Recipient output port
'''
class IRecipientOutputPort(metaclass=ABCMeta):

    @abstractmethod
    def get_recipient_by_id(self, recipient_id:str) -> Recipient:
        raise NotImplementedError()

    @abstractmethod
    def add_reservation(self, recipient:Recipient) -> bool:
        raise NotImplementedError()

