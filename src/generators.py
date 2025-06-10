def filter_by_currency(transactions, currency_code):
    """
    принимает список транзакций и нужную валюту, и возвращает итератор,
    выдающий только те транзакции, у которых валюта совпадает с заданной.
    """
    for transaction in transactions:
        # Проверяем наличие ключа operationAmount и вложенных данных
        if ('operationAmount' in transaction and
            'currency' in transaction['operationAmount'] and
                'code' in transaction['operationAmount']['currency']):
            # Если код валюты совпадает с заданным, возвращаем транзакцию
            if transaction['operationAmount']['currency']['code'] == currency_code:
                yield transaction


def transaction_descriptions(transactions):
    """
    Генератор, который по очереди возвращает описание каждой транзакции.

    :param transactions: список словарей с транзакциями
    """
    for transaction in transactions:
        # Описание хранится в ключе 'description'
        description = transaction.get('description', 'Нет описания')
        yield description


def card_number_generator(start, end):
    """
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    """
    for number in range(start, end + 1):
        # Форматируем число с ведущими нулями до 16 цифр
        card_number = f"{number: 016d}"
        # Разбиваем на группы по 4 цифры
        formatted_number = ' '.join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield formatted_number


transactions_1 = [
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
        # Транзакция другого типа валюты
        "id": 123456789,
        "state": "EXECUTED",
        'operationAmount': {
            'amount': '1000',
            'currency': {
                'name': 'EUR',
                'code': 'EUR'
            }
        }
    }
]


# Использование функции:
usd_transactions = filter_by_currency(transactions_1, 'USD')
for transaction_1 in usd_transactions:
    print(transaction_1)

print("")
print("")

descriptions = transaction_descriptions(transactions_1)
for transaction_2 in descriptions:
    print(transaction_2)

print("")
print("")

for card_number_1 in card_number_generator(1, 8):
    print(card_number_1)
