def get_mask_card_number(card_number: str) -> str:
    """
    Маскирует номер карты в формате: XXXX XX** **** XXXX
    - показываются первые 6 цифр и последние 4 цифры
    - остальные заменяются на звездочки
    - номер разбит по блокам по 4 цифры, разделенным пробелами
    """
    # Удаляем все пробелы для обработки
    clean_number = "".join(filter(str.isdigit, card_number))

    # Проверка длины номера
    if len(clean_number) < 10:
        # Если меньше 10 цифр, маскируем все полностью
        return " ".join(["X" * 4 for _ in range((len(clean_number) + 3) // 4)])

    # Первые 6 цифр
    first_part = clean_number[:6]
    # Последние 4 цифры
    last_part = clean_number[-4:]

    # Остальные цифры между ними — маскируем звездочками
    middle_length = len(clean_number) - 10
    # сколько символов между первым и последним блоком
    middle_mask = "*" * middle_length

    # Собираем полный маскированный номер без пробелов
    masked_full = first_part + middle_mask + last_part

    # Разбиваем на блоки по 4 символа для форматирования
    blocks = [masked_full[i : i + 4] for i in range(0, len(masked_full), 4)]

    return " ".join(blocks)


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер счета в формате: **XXXX,
    показывая только последние 4 цифры, перед которыми две звездочки.
    """
    # Удаляем все пробелы и дефисы для обработки
    clean_number = "".join(filter(str.isdigit, account_number))

    if len(clean_number) < 4:
        # Если меньше 4 цифр, маскируем полностью
        return "**" + clean_number

    last_four = clean_number[-4:]

    return "**" + last_four


# Проверка
print(get_mask_card_number("7000792289606361"))
print(get_mask_account("73654108430135874305"))
