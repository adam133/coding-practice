from decimal import Decimal

import pytest
from pydantic import ValidationError

from src.tip_calculator import TipCalculator

sample_input = {"bill_amount": 100, "tip_percentage": 12, "number_of_people": 3}


def test_tip_calculator_success():
    tip_calculator = TipCalculator(**sample_input)
    assert tip_calculator.calculate_tip == Decimal("12.00")
    assert tip_calculator.calculate_total == Decimal("112.00")
    assert tip_calculator.calculate_total_per_person == Decimal("37.33")


def test_bill_amount_failure():
    with pytest.raises(ValidationError):
        TipCalculator(bill_amount=-100, tip_percentage=12, number_of_people=3)


def test_tip_percentage_failure():
    with pytest.raises(ValidationError):
        TipCalculator(bill_amount=100, tip_percentage=-12, number_of_people=3)


def test_tip_percentage_failure():
    with pytest.raises(ValidationError):
        TipCalculator(bill_amount=100, tip_percentage=-12, number_of_people=3)


def test_number_of_people_failure():
    with pytest.raises(ValidationError):
        TipCalculator(bill_amount=100, tip_percentage=12, number_of_people=-3)


def test_number_of_people_zero_failure():
    with pytest.raises(ValidationError):
        TipCalculator(bill_amount=100, tip_percentage=12, number_of_people=0)
