# Создать декоратор для использования кэша. Т.е. сохранять аргументы и результаты в словарь, если вызывается функция с агрументами, 
# которые уже записаны в кэше - вернуть результат из кэша, если нет - выполнить функцию. Кэш лучше хранить в json.
# Решение, близкое к решению данной задачи было разобрано на семинаре.

import json
from functools import wraps

def cache_result(func):
    cache = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        cache_key = json.dumps((args, kwargs))
        result = cache.get(cache_key)

        if result is None:
            result = func(*args, **kwargs)
            cache[cache_key] = result

        return result

    return wrapper


@cache_result
def calculate_square(x):
    return x ** 2

@cache_result
def multiply(a, b):
    return a * b

print(calculate_square(3))  # Вычисляет результат и кеширует
print(calculate_square(3))  # Возвращает закешированный результат

print(multiply(4, 5))  # Вычисляет результат и кеширует
print(multiply(4, 5))  # Возвращает закешированный результат