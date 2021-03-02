import math
from math import trunc

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    amount = math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
    value = trunc(amount * 100) / 100
    return value

def test_get_age_carbon_14_dating():
    carbon_14_ratio = 0.35
    assert get_age_carbon_14_dating(carbon_14_ratio) == 8680.34

# def test_get_negative_carbon_14_dating():
#     carbon_14_ratio = -0.35
#     assert get_age_carbon_14_dating(carbon_14_ratio) == print("invalid")