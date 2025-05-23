from datetime import datetime

import src.masks


def get_date(date_str: str) -> str:
    """
    Преобразует формат даты в более читаемый
    """
    # Парсим строку с помощью strptime
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    # Форматируем дату в нужный формат
    return dt.strftime("%d.%m.%Y")


def mask_account_card(info: str) -> str:
    """
    Обрабатывает строку с типом и номером карты или счета.

    Примеры входных данных:
      - "Visa Platinum 7000792289606361"
      - "Maestro 7000792289606361"
      - "Счет 73654108430135874305"

    Возвращает строку с маскированным номером в нужном формате.
    """
    # Разделяем строку на части
    parts = info.strip().split()

    # Определяем тип (первый элемент)
    type_str = parts[0]

    # Остальные части — номер или название типа + номер
    # Предположим, что тип может быть "Visa", "Maestro" или "Счет"

    if type_str.lower() == "счет":
        # Обработка счета
        account_number = " ".join(parts[1:])
        masked = src.masks.get_mask_account(account_number)
        return f"{type_str} {masked}"

    else:
        # Обработка карты
        # Предположим, что название карты могут состоять из нескольких слов
        # Тогда нужно определить границу между названием и номером.
        # номер обычно справа.

        card_type = " ".join(parts[:-1])  # все кроме последнего
        card_number = parts[-1]

        masked = src.masks.get_mask_card_number(card_number)
        return f"{card_type} {masked}"
