import pytest
import sys
from datetime import datetime

sys.path.append("./src/")

from slot import Slot 

slot_id = "1"
dt_slot = datetime(2021, 11, 12, 10, 0, 0)
location = "Tokyo"

@pytest.fixture()
def fixture_slot():
    return Slot(slot_id, dt_slot, location)

def test_new_slot(fixture_slot):

    target = fixture_slot
    assert target != None
    assert slot_id == target.slot_id
    assert dt_slot == target.reservation_date
    assert location == target.location
    assert True == target.is_vacant

def test_use_slot(fixture_slot):
    target = fixture_slot
    assert True == target.is_vacant
    target.use_slot()
    assert False == target.is_vacant