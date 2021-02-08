# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}



def generate_trunk_config(intf_vlan_mapping:dict, trunk_template:list)->dict:
    '''
    Функция генерирует конфигурацию транков.

    - intf_vlan_mapping: словарь с соответствием интерфейс-VLANы такого вида:
        {'FastEthernet0/1': [10, 20],
         'FastEthernet0/2': [11, 30],
         'FastEthernet0/4': [17]}
    - trunk_template: шаблон конфигурации trunk-портов в виде списка команд (список trunk_mode_template)

    Возвращает словарь:
    - ключи: имена интерфейсов, вида 'FastEthernet0/1'
    - значения: список команд, который надо выполнить на этом интерфейсе
    '''
    dict_config_interfaces = {}
    for intf, vlans in intf_vlan_mapping.items():
        list_config_interfaces = []
        for cmd in trunk_template:
            if cmd.endswith('allowed vlan'):
                vlans = [str(i) for i in vlans]
                cmd = f'{cmd} {",".join(vlans)}'
            list_config_interfaces.append(cmd)
        dict_config_interfaces[intf] = list_config_interfaces
    return dict_config_interfaces 

if __name__ == '__main__':
    print(generate_trunk_config(trunk_config, trunk_mode_template))
