import pytest
import sys
from datetime import datetime

sys.path.append("./src/")

from recipient import Recipient
from slot import Slot

recipient_id = "1"
email = "fatsushi@example.com"
first_name = "Atsushi"
last_name = "Fukui"
age = 30
dt_slot = datetime(2021, 11, 12, 10, 0, 0)
dt_slot_2 = datetime(2021, 12, 10, 10, 0, 0)
dt_slot_3 = datetime(2021, 12, 31, 10, 0, 0)
location = "Tokyo"


@pytest.fixture()
def fixture_recipient():
    return Recipient(recipient_id, email, first_name, last_name, age)    

@pytest.fixture()
def fixture_slot():
    return Slot("1", dt_slot, location)

@pytest.fixture()
def fixture_slot_2():
    return Slot("2", dt_slot_2, location)

@pytest.fixture()
def fixture_slot_3():
    return Slot("3", dt_slot_3, location)

def test_new_recipient(fixture_recipient):

    target = fixture_recipient
    assert target != None
    assert recipient_id == target.recipient_id
    assert email == target.email
    assert first_name == target.first_name
    assert last_name == target.last_name
    assert age == target.age
    assert target.slots != None
    assert 0 == len(target.slots)

def test_add_slot_one(fixture_recipient, fixture_slot):
    slot = fixture_slot
    target = fixture_recipient
    target.add_reserve_slot(slot)
    assert slot != None
    assert target != None
    assert 1 == len(target.slots)
    assert slot.slot_id == target.slots[0].slot_id
    assert slot.reservation_date == target.slots[0].reservation_date
    assert slot.location == target.slots[0].location
    assert False == target.slots[0].is_vacant

def test_add_slot_two(fixture_recipient, fixture_slot, fixture_slot_2):
    slot = fixture_slot
    slot2 = fixture_slot_2
    target = fixture_recipient
    target.add_reserve_slot(slot)
    target.add_reserve_slot(slot2)
    assert 2 == len(target.slots)

def test_cannot_append_slot_more_than_two(fixture_recipient, fixture_slot, fixture_slot_2, fixture_slot_3):
    slot = fixture_slot
    slot2 = fixture_slot_2
    slot3 = fixture_slot_3
    target = fixture_recipient
    target.add_reserve_slot(slot)
    target.add_reserve_slot(slot2)
    ret = target.add_reserve_slot(slot3)
    assert False == ret
    assert 2 == len(target.slots)

def test_cannot_append_same_date_slot(fixture_recipient, fixture_slot):
    slot = fixture_slot
    target = fixture_recipient
    target.add_reserve_slot(slot)
    ret = target.add_reserve_slot(slot)
    assert False == ret
    assert 1 == len(target.slots)
