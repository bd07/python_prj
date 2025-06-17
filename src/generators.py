from typing import Generator


def filter_by_currency(transactions: list, currency_code: str) -> Generator[dict, None, None]:
    """
    принимает список транзакций и нужную валюту,
    и возвращает итератор по транзакциям с совпадающим кодом валюты.
    """
    # Проверка на пустоту и ноль
    if transactions not in ("", "0"):
        for transaction_1 in transactions:
            # Проверяем наличие ключа operationAmount и вложенных данных
            if (
                "operationAmount" in transaction_1
                and "currency" in transaction_1["operationAmount"]
                and "code" in transaction_1["operationAmount"]["currency"]
            ):
                # Если код валюты совпадает с заданным, возвращаем транзакцию
                if transaction_1["operationAmount"]["currency"]["code"] == currency_code:
                    yield transaction_1


def transaction_descriptions(transactions: list) -> Generator[str, None, None]:
    """
    Генератор, который по очереди возвращает описание каждой транзакции.
    """
    # Проверка на пустоту и ноль
    if transactions not in ("", "0"):
        for transaction_1 in transactions:
            # Описание хранится в ключе 'description'
            description = transaction_1.get("description", "Нет описания")
            yield description


def card_number_generator(start: int, end: int) -> str:
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    if end not in ("", "0"):
        result = ""
        for number in range(start, end + 1):
            # Форматируем число с ведущими нулями до 16 цифр
            card_number = f"{number:016d}"
            # Разбиваем на группы по 4 цифры
            formatted_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
            result += formatted_number + ", "
        return result
    else:
        return "0"


transactions_1 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        # Транзакция другого типа валюты
        "id": 123456789,
        "state": "EXECUTED",
        "operationAmount": {"amount": "1000", "currency": {"name": "EUR", "code": "EUR"}},
    },
]


# Создаем итератор для транзакций в USD
usd_transactions = filter_by_currency(transactions_1, "USD")

for transaction in usd_transactions:
    print(transaction)

print("")
print("")

var_transaction_descriptions = transaction_descriptions(transactions_1)
for var_transaction_description in var_transaction_descriptions:
    print(var_transaction_description)

print("")
print("")

print(card_number_generator(1, 5))
