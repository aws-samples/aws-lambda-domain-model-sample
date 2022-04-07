import pytest
import sys

sys.path.append("./src/")

from i_recipient_adapter import IRecipientAdapter
from recipient_output_port import RecipientOutputPort
from recipient import Recipient

#value for testing
recipient_id = "1"
email = "fatsushi@example.com"
first_name = "Atsushi"
last_name = "Fukui"
age = 30

# Dummy class for RecipientAdapter
class DummyRecipientAdapter(IRecipientAdapter):
    def load(self, recipient_id:str) -> Recipient:
        return Recipient(recipient_id, email, first_name, last_name, age)

    def save(self, recipient:Recipient) -> bool:
        return True


@pytest.fixture()
def fixture_recipient_output_port():
    
    #SetUp
    recipient_output_port = RecipientOutputPort(DummyRecipientAdapter())

    #execute testing
    yield recipient_output_port

    #TearDown
    recipient_output_port = None

def test_recipient_port_recipient_by_id(fixture_recipient_output_port):
    target = fixture_recipient_output_port
    recipient_id = "dummy_number"
    recipient = target.get_recipient_by_id(recipient_id)
    assert recipient != None
    assert email == recipient.email
    assert first_name == recipient.first_name
    assert last_name == recipient.last_name
    assert age == recipient.age


def test_recipient_port_add_reservation_must_be_true(fixture_recipient_output_port):
    target = fixture_recipient_output_port
    ret = target.add_reservation(Recipient(recipient_id, email, first_name, last_name, age))
    assert True == ret
