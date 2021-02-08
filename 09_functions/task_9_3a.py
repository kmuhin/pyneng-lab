# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


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
        vlan = ''
        for line in f:
            if line.startswith('!') and intf:
                if intf and not vlan:
                    config_intf_access[intf] = 1
                intf = ''
                vlan = ''
                continue
            if 'Ethernet' in line:
                _, intf = line.split()
            elif intf and 'access vlan' in line:
                _, vlan = line.rsplit(maxsplit=1)
                config_intf_access[intf] = int(vlan)
            elif intf and 'trunk allowed' in line:
                _, vlan= line.rsplit(maxsplit=1)
                vlans = [int(vl) for vl in vlan.split(',')]
                config_intf_trunk[intf] = vlans
    return config_intf_access, config_intf_trunk

if __name__ == '__main__':
    config_access, config_trunk = get_int_vlan_map('config_sw1.txt')
    print(config_access)
    print(config_trunk)

