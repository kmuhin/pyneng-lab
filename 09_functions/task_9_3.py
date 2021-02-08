# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


def get_int_vlan_map(config_filename:str):
    '''
    Функция обрабативает файл конфигурации и возвращает кортеж из двух словарей.

    config_filename - имя файла конфигурации

    возвращает кортеж из двух словарей:
    * словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/16': 17}
    * словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
    {'FastEthernet0/1': [10, 20],
     'FastEthernet0/2': [11, 30],
     'FastEthernet0/4': [17]}
    '''
    config_intf_access = {}
    config_intf_trunk = {}
    with open(config_filename) as f:
        intf = ''
        for line in f:
            if line.startswith('!') and intf:
                intf = ''
                continue
            if line.startswith('interface'):
                _, intf = line.split()
            elif intf and 'access vlan' in line:
                _, vlan = line.rsplit(maxsplit=1)
                config_intf_access[intf] = int(vlan)
            elif intf and 'trunk allowed' in line:
                _, vlans = line.rsplit(maxsplit=1)
                vlans = [int(vlan) for vlan in vlans.split(',')]
                config_intf_trunk[intf] = vlans
    return config_intf_access, config_intf_trunk

if __name__ == '__main__':
    print(get_int_vlan_map('config_sw1.txt'))

