import pytest


@pytest.fixture
def card():
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def rs():
    return "Счет **4305"


@pytest.fixture
def zero():
    return "0"


@pytest.fixture
def date():
    return "11.03.2024"


@pytest.fixture
def answer_8():
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def answer_9():
    return [
        {"id": 41428820, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def answer_10():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "0"},
    ]


@pytest.fixture
def answer_11():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428820, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def answer_12():
    return [
        {"id": 41428820, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
