import pytest
from utils import read_file, filter_operations, converte_date, format_card, the_result


def test_read_file():
    pass


def test_filter_operations(fixture_filter_operations):
    assert len(filter_operations(fixture_filter_operations)) == 1


def test_converte_date():
    assert converte_date("2018-09-12T21:27:25.241689") == "12.09.2018"


def test_format_card():
    assert format_card("Visa Platinum 1246377376343588") == "Visa Platinum 1246 37** **** 3588"
    assert format_card("Счет 14211924144426031657") == "Счет **1657"


def test_the_result(fixture_one_operation):
    assert the_result(fixture_one_operation) == "14.10.2018 Перевод организации\n" \
                                                "Visa Platinum 2256 48** **** 2539 -> Счет **9319\n" \
                                                "90582.51 USD\n"
