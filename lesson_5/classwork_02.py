"""
Создать функцию, которая принимает на вход неопределенное количество аргументов
и возвращает их сумму и максимальное из них.
"""


def sum_max(*args):
    result_sum = 0
    max_item = args(0)
    for item in args:
        result_sum += item

        if item > max_item:
            max_item = item
    return result_sum, max_item

print(sum_and_max(1, 10, 20, 50, 60))
