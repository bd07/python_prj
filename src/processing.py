def filter_by_state(records, state="EXECUTED"):
    """
    Возвращает новый список словарей, у которых ключ 'state' равен указанному значению.
    """
    return [record for record in records if record.get("state") == state]


def sort_by_date(records, reverse=True):
    """
    Возвращает новый список словарей, отсортированный по ключу 'date'.
    """
    return sorted(records, key=lambda x: x.get("date", ""), reverse=reverse)
