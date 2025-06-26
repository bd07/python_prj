import sys


def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Открываем лог-файл или используем stdout
            if filename:
                log_stream = open(filename, 'a', encoding='utf-8')
            else:
                log_stream = sys.stdout

            # Логируем начало выполнения функции
            print(f"{func.__name__} start", file=log_stream)

            try:
                result = func(*args, **kwargs)
                # Логируем успешное завершение
                print(f"{func.__name__} ok", file=log_stream)
                return result
            except Exception as e:
                # Логируем ошибку и входные параметры
                error_type = type(e).__name__
                print(f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}", file=log_stream)
                raise
            finally:
                if filename:
                    log_stream.close()
        return wrapper
    return decorator


# Проверка кода
@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


print(my_function(2, 4))
