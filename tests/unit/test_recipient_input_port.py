import pytest
import sys
from datetime import datetime

sys.path.append("./src/")

from i_recipient_output_port import IRecipientOutputPort
from i_slot_output_port import ISlotOutputPort
from recipient_input_port import RecipientInputPort
from recipient import Recipient
from slot import Slot
from status import Status

recipient_id = "1"
email = "fatsushi@example.com"
first_name = "Atsushi"
last_name = "Fukui"
age = 61
slot_id = "1"
reservation_date = datetime(2021,12,20, 9, 0, 0)
location = "Tokyo"


class DummyRecipientOutputPort(IRecipientOutputPort):
    def get_recipient_by_id(self, recipient_id:str) -> Recipient:
        return Recipient(recipient_id, email, first_name, last_name, age)

    def add_reservation(self, recipient:Recipient) -> bool:
        return True


class DummySlotOutputPort(ISlotOutputPort):
    def get_slot_by_id(self, slot_id:str) -> Slot:
        return Slot(slot_id, reservation_date, location)


@pytest.fixture()
def fixture_recipient_input_port():
    #SetUp
    recipient_input_port = RecipientInputPort(DummyRecipientOutputPort(), DummySlotOutputPort())

    #execute testing
    yield recipient_input_port

    #TearDown
    recipient_input_port = None

def test_add_reservation(fixture_recipient_input_port):
    target = fixture_recipient_input_port

    recipient_id = "dummy_id"
    slot_id = "dummy_id"

    status = target.make_reservation(recipient_id, slot_id)
    assert 200 == status.status_code
    assert "The recipient's reservation is added." == status.message


