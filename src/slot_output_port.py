from slot import Slot
from i_slot_output_port import ISlotOutputPort
from i_slot_adapter import ISlotAdapter

class SlotOutputPort(ISlotOutputPort):
    def __init__(self, adapter:ISlotAdapter):
        self.__adapter = adapter

    def get_slot_by_id(self, slot_id:str) -> Slot:
        return self.__adapter.load(slot_id)
