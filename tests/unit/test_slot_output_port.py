import pytest
import sys
from datetime import datetime

sys.path.append("./src/")

from i_slot_adapter import ISlotAdapter
from slot_output_port import SlotOutputPort
from slot import Slot

# value for testing
slot_id = "1"
reservation_date = datetime(2021,12,20, 9, 0, 0)
location = "Tokyo"


class DummySlotAdapter(ISlotAdapter):
    def load(self, slot_id:str) -> Slot:
        return Slot(slot_id, reservation_date, location)


@pytest.fixture()
def fixture_slot_output_port():

    #SetUp
    slot_output_port = SlotOutputPort(DummySlotAdapter())

    # execute testing
    yield slot_output_port

    #TearDown
    slot_output_port = None


def test_slot_output_port_slot_by_id(fixture_slot_output_port):
    target = fixture_slot_output_port
    slot_id = "1"
    slot = target.get_slot_by_id(slot_id)
    assert slot != None
    assert reservation_date == slot.reservation_date
    assert location == slot.location

