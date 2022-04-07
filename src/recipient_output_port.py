from recipient import Recipient
from i_recipient_output_port import IRecipientOutputPort
from i_recipient_adapter import IRecipientAdapter

'''
implementation of Recipient output port
'''
class RecipientOutputPort(IRecipientOutputPort):
    def __init__(self, adapter:IRecipientAdapter):
       self.__adapter = adapter

    def get_recipient_by_id(self, recipient_id:str) -> Recipient:
        return self.__adapter.load(recipient_id)
    
    def add_reservation(self, recipient:Recipient) -> bool:
        return self.__adapter.save(recipient)
