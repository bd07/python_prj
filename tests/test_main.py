import pytest

import src.processing
import src.widget


# Маскировка карты, счета
@pytest.mark.parametrize('card, mask_kard', [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("", "0"),
    ("0", "0")
])
def test_mask_account_card(card, mask_kard):
    assert src.widget.mask_account_card(card) == mask_kard


# Преобразование дат
def test_get_date(date):
    assert src.widget.get_date("2024-03-11T02:26:18.671403") == date


def test_get_date_zero(zero):
    assert src.widget.get_date("0") == zero


def test_get_date_empty(zero):
    assert src.widget.get_date("") == zero


data1 = [
    {"id": 41428820, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
data1_empty_zero = [
    {"id": 41428820, "state": "", "date": ""},
    {"id": 939719570, "state": "EXECUTED", "date": "0"},
    {"id": 594226727, "state": "CANCELED", "date": "0"},
    {"id": 615064591, "state": "CANCELED_AAA", "date": ""},
]


# Фильтр
def test_filter_by_state_canceled(answer_8):
    assert src.processing.filter_by_state(data1, "CANCELED") == answer_8


def test_filter_by_state_executed(answer_9):
    assert src.processing.filter_by_state(data1, "EXECUTED") == answer_9


def test_filter_by_state_zero(answer_10):
    assert src.processing.filter_by_state(data1_empty_zero, "EXECUTED") == answer_10


# Сортировка
def test_sort_by_date_reverse(answer_11):
    assert src.processing.sort_by_date(data1, reverse=False) == answer_11


def test_sort_by_date_ss(answer_12):
    assert src.processing.sort_by_date(data1) == answer_12
