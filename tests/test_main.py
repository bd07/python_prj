import pytest

import src.processing
import src.widget
import src.generators
import src.decorators


# Маскировка карты, счета
@pytest.mark.parametrize('card, mask_kard', [
    ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
    ("Счет 73654108430135874305", "Счет **4305"),
    ("", "0"),
    ("0", "0")
])
def test_mask_account_card(card, mask_kard):
    """ Проверка функции маскировки номеров счетов и карт"""
    assert src.widget.mask_account_card(card) == mask_kard


# Преобразование дат
def test_get_date(date):
    """ Проверка функции для преобразования даты"""
    assert src.widget.get_date("2024-03-11T02:26:18.671403") == date


def test_get_date_zero(zero):
    """ Проверка функции для преобразования даты с нулевым значением"""
    assert src.widget.get_date("0") == zero


def test_get_date_empty(zero):
    """ Проверка функции для преобразования даты с пустым значением"""
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
    """ Проверка функции для фильтрации данных"""
    assert src.processing.filter_by_state(data1, "CANCELED") == answer_8


def test_filter_by_state_executed(answer_9):
    """ Проверка функции для фильтрации данных с пустым значением"""
    assert src.processing.filter_by_state(data1, "EXECUTED") == answer_9


def test_filter_by_state_zero(answer_10):
    """ Проверка функции для фильтрации данных с нулевым значением"""
    assert src.processing.filter_by_state(data1_empty_zero, "EXECUTED") == answer_10


# Сортировка
def test_sort_by_date_reverse(answer_11):
    """ Проверка функции для сортировки данных"""
    assert src.processing.sort_by_date(data1, reverse=False) == answer_11


def test_sort_by_date_ss(answer_12):
    """ Проверка функции для сортировки данных"""
    assert src.processing.sort_by_date(data1) == answer_12


transactions = (
    [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

answer_13 = (
    [
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

answer_14 = [
    "Перевод организации",
    "Перевод со счета на счет",
    "Перевод со счета на счет",
    "Перевод с карты на карту",
    "Перевод организации"
]


@pytest.mark.parametrize('transactions_1, currency_code', [
    (transactions, answer_13),
    ("0", []),
    ("", [])
])
def test_filter_by_currency(transactions_1, currency_code):
    """ Проверка функции для фильтрации данных"""
    result = list(src.generators.filter_by_currency(transactions_1, "RUB"))
    assert result == currency_code


@pytest.mark.parametrize('transactions_1, currency_code', [
    (transactions, answer_14),
    ("0", []),
    ("", [])
])
def test_transaction_descriptions(transactions_1, currency_code):
    """ Проверка функции для вывода описания транзакции"""
    result = list(src.generators.transaction_descriptions(transactions_1))
    assert result == currency_code


@pytest.mark.parametrize('end, currency_code', [
    ("", "0"),
    (4, "0000 0000 0000 0001, 0000 0000 0000 0002, 0000 0000 0000 0003, 0000 0000 0000 0004, ")
])
def test_card_number_generator(end, currency_code):
    """ Проверка функции для генерации номеров карт"""
    assert src.generators.card_number_generator(1, end) == currency_code


def example_function():
    raise Exception("Max retries exceeded")


def test_my_function():
    with pytest.raises(Exception, match="Max retries exceeded"):
        example_function()
