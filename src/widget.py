from datetime import datetime




def get_date(date_str):
    """
    Преобразует формат даты в более читаемый
    """
    # Парсим строку с помощью strptime
    dt = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    # Форматируем дату в нужный формат
    return dt.strftime("%d.%m.%Y")

# Пример использования функции get_date:
date_input = "2024-03-11T02:26:18.671407"
print(get_date(date_input))  # Выведет: 11.03.2024