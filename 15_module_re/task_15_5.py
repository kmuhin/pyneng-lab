# -*- coding: utf-8 -*-
"""
Задание 15.5

Создать функцию generate_description_from_cdp, которая ожидает как аргумент
имя файла, в котором находится вывод команды show cdp neighbors.

Функция должна обрабатывать вывод команды show cdp neighbors и генерировать на основании вывода команды описание для интерфейсов.

Например, если у R1 такой вывод команды:
R1>show cdp neighbors
Capability Codes: R - Router, T - Trans Bridge, B - Source Route Bridge
                  S - Switch, H - Host, I - IGMP, r - Repeater

Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID
SW1              Eth 0/0           140          S I      WS-C3750-  Eth 0/1

Для интерфейса Eth 0/0 надо сгенерировать такое описание
description Connected to SW1 port Eth 0/1

Функция должна возвращать словарь, в котором ключи - имена интерфейсов, а значения - команда задающая описание интерфейса:
'Eth 0/0': 'description Connected to SW1 port Eth 0/1'


Проверить работу функции на файле sh_cdp_n_sw1.txt.
"""

import re


def generate_description_from_cdp(filename):
    """
    parsing command show cdp neighbors from file

    input
        filename - name of command output file
    output
        dictionary:
            {"Eth 0/1": "description Connected to R1 port Eth 0/0", "Eth 0/2": "description Connected to R2 port Eth 0/0"}
    """
    neighbors_description = {}
    reg_neighbors = re.compile(r'(?P<dev_neighb>^\S+) +'
                               r'(?P<int_local>\w+ \S+) +'
                               r'\d+ +((?:\w )+) +\d+ +'
                               r'(?P<int_neighb>\w+ \S+)$')
    template_description = 'description Connected to {dev_neighb} port {int_neighb}'
    with open(filename) as f:
        for line in f:
            match = reg_neighbors.search(line)
            if match:
                description = template_description.format(**match.groupdict())
                neighbors_description[match.group('int_local')] = description
    return neighbors_description


if __name__ == '__main__':
    print(generate_description_from_cdp('sh_cdp_n_sw1.txt'))
