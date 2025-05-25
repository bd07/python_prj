import src.processing
import src.widget


# Маскировка карты, счета
rs_1 = "Visa Platinum 7000792289606361"
answer_1 = "Visa Platinum 7000 79** **** 6361"
rs_2 = "Счет 73654108430135874305"
answer_2 = "Счет **4305"
zero = "0"
empty = ""


def test_mask_account_card():
    assert src.widget.mask_account_card(rs_1) == answer_1
    assert src.widget.mask_account_card(rs_2) == answer_2
    assert src.widget.mask_account_card(zero) == zero
    assert src.widget.mask_account_card(empty) == zero


# Преобразование дат
date_str_1 = "2024-03-11T02:26:18.671403"
answer_5 = "11.03.2024"


def test_get_date():
    assert src.widget.get_date(date_str_1) == answer_5
    assert src.widget.get_date(empty) == zero
    assert src.widget.get_date(zero) == zero


data1 = [
    {"id": 41428820, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
answer_8 = [
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]
answer_9 = [
    {"id": 41428820, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]
data1_empty_zero = [
    {"id": 41428820, "state": "", "date": ""},
    {"id": 939719570, "state": "EXECUTED", "date": "0"},
    {"id": 594226727, "state": "CANCELED", "date": "0"},
    {"id": 615064591, "state": "CANCELED_AAA", "date": ""},
]
answer_10 = [
    {"id": 939719570, "state": "EXECUTED", "date": "0"},
]


# Фильтр
def test_filter_by_state():
    assert src.processing.filter_by_state(data1, "CANCELED") == answer_8
    assert src.processing.filter_by_state(data1, "EXECUTED") == answer_9
    assert src.processing.filter_by_state(data1_empty_zero, "EXECUTED") == answer_10


answer_11 = [
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 41428820, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
]
answer_12 = [
    {"id": 41428820, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
]


# Сортировка
def test_sort_by_date():
    assert src.processing.sort_by_date(data1, reverse=False) == answer_11
    assert src.processing.sort_by_date(data1) == answer_12
