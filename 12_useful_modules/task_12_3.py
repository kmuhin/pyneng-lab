# -*- coding: utf-8 -*-
"""
Задание 12.3


Создать функцию print_ip_table, которая отображает таблицу доступных и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

Функция не должна изменять списки, которые переданы ей как аргументы.
То есть, до выполнения функции и после списки должны выглядеть одинаково.


Для этого задания нет тестов
"""

from tabulate import tabulate


def print_ip_table(reachable_addresses, unreachable_addresses):
    columns = ['Reachable', 'Unreachable']
    max_len = max(len(reachable_addresses), len(unreachable_addresses))
    # Extend both lists to max len with None.
    list_reachable = reachable_addresses[:] + [None] * (max_len - len(reachable_addresses))
    list_unreachable = unreachable_addresses[:] + [None] * (max_len - len(unreachable_addresses))
    print(tabulate(zip(list_reachable, list_unreachable), headers=columns))


if __name__ == '__main__':
    reachable = ['1.1.1.1', '8.8.8.8']
    unreachable = ['aaa', '5.1.1', '270.1.1.1']
    print_ip_table(reachable, unreachable)
