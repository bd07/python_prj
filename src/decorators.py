import sys
from datetime import datetime


def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Открываем лог-файл или используем stdout
            if filename:
                log_stream = open(filename, "a", encoding="utf-8")
            else:
                log_stream = sys.stdout

            # Логируем начало выполнения функции
            now = datetime.now()
            formatted_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{formatted_date_time} {func.__name__} запущена", file=log_stream)

            try:
                result = func(*args, **kwargs)
                # Логируем успешное завершение
                print("функция выполнена", file=log_stream)
                return result
            except Exception as e:
                # Логируем ошибку и входные параметры
                error_type = type(e).__name__
                print(f"у функции ошибка: {error_type} //{args}, {kwargs}", file=log_stream)
                raise
            finally:
                if filename:
                    log_stream.close()

        return wrapper

    return decorator
