import src.processing
import src.widget


# Маскировка карты, счета
rs_1 = "Visa Platinum 7000792289606361"
answer_1 = "Visa Platinum 7000 79** **** 6361"
rs_2 = "Счет 73654108430135874305"
answer_2 = "Счет **4305"
rs_3 = "0"
answer_3 = "0"
rs_4 = ""
answer_4 = "0"


def test_mask_account_card():
    assert src.widget.mask_account_card(rs_1) == answer_1
    assert src.widget.mask_account_card(rs_2) == answer_2
    assert src.widget.mask_account_card(rs_3) == answer_3
    assert src.widget.mask_account_card(rs_4) == answer_4


# Преобразование дат
date_str_1 = "2024-03-11T02:26:18.671403"
answer_5 = "11.03.2024"
date_str_2 = "0"
answer_6 = "0"
date_str_3 = ""
answer_7 = "0"


def test_get_date():
    assert src.widget.get_date(date_str_1) == answer_5
    assert src.widget.get_date(date_str_2) == answer_6
    assert src.widget.get_date(date_str_3) == answer_7


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


# Фильтр
def test_filter_by_state():
    assert src.processing.filter_by_state(data1, "CANCELED") == answer_8
    assert src.processing.filter_by_state(data1, "EXECUTED") == answer_9


# Сортировка по возрастанию
sorted_asc = src.processing.sort_by_date(data1, reverse=False)
print(sorted_asc)
