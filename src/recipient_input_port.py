from i_recipient_input_port import IRecipientInputPort
from i_recipient_output_port import IRecipientOutputPort
from i_slot_output_port import ISlotOutputPort
from status import Status


'''
implementation of Recipient input port
'''
class RecipientInputPort(IRecipientInputPort):
    def __init__(self, recipient_output_port: IRecipientOutputPort, slot_output_port: ISlotOutputPort):
        self.__recipient_output_port = recipient_output_port
        self.__slot_output_port = slot_output_port

    '''
    make reservation: adapting domain model business logic
    '''
    def make_reservation(self, recipient_id:str, slot_id:str) -> Status:
        status = None        
        
        # ---------------------------------------------------
        # get an instance from output port
        # ---------------------------------------------------
        recipient = self.__recipient_output_port.get_recipient_by_id(recipient_id)
        slot = self.__slot_output_port.get_slot_by_id(slot_id)

        if recipient == None or slot == None:
            return Status(400, "Request instance is not found. Something wrong!")

        print(f"recipient: {recipient.first_name}, slot date: {slot.reservation_date}")

        # ---------------------------------------------------
        # execute domain logic
        # ---------------------------------------------------
        ret = recipient.add_reserve_slot(slot)

        # ---------------------------------------------------
        # persistent an instance throgh output port
        # ---------------------------------------------------
        if ret == True:
            ret = self.__recipient_output_port.add_reservation(recipient)

        if ret == True:
            status = Status(200, "The recipient's reservation is added.")
        else:
            status = Status(200, "The recipient's reservation is NOT added!")
        return status
