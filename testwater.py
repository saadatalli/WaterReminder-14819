import pytest
from water_reminder import calculate_water_intake

def test_water_intake_calculation():
    assert calculate_water_intake(60, 25) == (1.98, 2)
    assert calculate_water_intake(30, 15) == (0.99, 3)
    assert calculate_water_intake(70, 60) == (2.31, 1.5)

def test_negative_input():
    with pytest.raises(ValueError):
        calculate_water_intake(-10, 25)
    with pytest.raises(ValueError):
        calculate_water_intake(50, -5)
