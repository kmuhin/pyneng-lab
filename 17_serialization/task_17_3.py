# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""

import re

regex_cdp_nbr = re.compile(r'(?P<dev_neighb>^\S+)\s+'
                           r'(?P<int_local>\w+ \S+)\s+'
                           r'\d+\s+((?:\w )+)\s+\S+\s+'
                           r'(?P<int_neighb>\w+ \S+)$')
regex_cdp_dev = re.compile(r'(?P<dev>\S+)>sh')


def parse_sh_cdp_neighbors(text):
    """
    parsing command output "show cdp neighbors"

    :param text: command output "show cdp neighbors" as str
    :return: dict {'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
                         'Fa 0/2': {'R6': 'Fa 0/0'}}}
    """
    result = {}
    dev = ''
    for line in text.split('\n'):
        match = regex_cdp_dev.search(line)
        if match:
            dev = match.group(1)
            result[dev] = {}
            continue
        match = regex_cdp_nbr.search(line)
        if match and dev:
            result[dev][match.group('int_local')] = {match.group('dev_neighb'): match.group('int_neighb')}
    return result


if __name__ == '__main__':
    with open('sh_cdp_n_sw1.txt') as f:
        print(parse_sh_cdp_neighbors(f.read()))
