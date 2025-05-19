def filter_by_state(records, state='EXECUTED'):
    """
    Возвращает новый список словарей, у которых ключ 'state' равен указанному значению.
    """
    return [record for record in records if record.get('state') == state]


def sort_by_date(records, reverse=True):
    """
    Возвращает новый список словарей, отсортированный по ключу 'date'.
    """
    return sorted(records, key=lambda x: x.get('date', ''), reverse=reverse)


data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
 ]

# По умолчанию фильтр по статусу 'EXECUTED'
#print(filter_by_state(data))

# Фильтр по статусу 'CANCELED'
#print(filter_by_state(data, 'CANCELED'))

# Сортировка по возрастанию
sorted_asc = sort_by_date(data, reverse=False)
print(sorted_asc)