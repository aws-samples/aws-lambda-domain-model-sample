import pytest
import sys

sys.path.append("./src/")

from status import Status 

# @pytest.fixture()
# def myfixture():
#   return ''

def test_set_status_properties():
    status_code = 200
    message = "hello"

    target = Status(status_code, message)
    assert status_code == target.status_code
    assert message == target.message
