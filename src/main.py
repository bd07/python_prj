import src.processing
import src.widget

# Маскировка номера карты
cerd = "Visa Platinum 7000792289606361"
print(src.widget.mask_account_card(cerd))

# Маскировка счета
rs = "Счет 73654108430135874305"
print(src.widget.mask_account_card(rs))

# Преобразование даты
date_input = "2024-03-11T02:26:18.671407"
print(src.widget.get_date(date_input))

data = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

# Фильтр по статусу 'CANCELED'
print(src.processing.filter_by_state(data, "CANCELED"))

# Сортировка по возрастанию
sorted_asc = src.processing.sort_by_date(data, reverse=False)
print(sorted_asc)
