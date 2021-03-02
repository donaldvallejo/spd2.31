import pytest
import extract_position_function as e4


@pytest.fixture
def average_input():
    return "|update| the positron location \
            particle accelerator is x:21.432"


@pytest.fixture
def null_input():
    """For whatever reason its null."""
    return None


@pytest.fixture
def error_input():
    """Something went wrong with the machine, so the log reports an error."""
    return "|error| calculation no work."

def test_null_case(null_input):
    """Reads in a log that's None"""
    # NoneType Input
    assert e4.extract_position(null_input) == None

def test_average_case(average_input):
    """Reads in a log from the device, and returns
    the location of the positron (if mentioned)."""
    # Expected Input - contains 'x:
    assert e4.extract_position(average_input) == "21.432"