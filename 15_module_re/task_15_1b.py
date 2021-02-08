# -*- coding: utf-8 -*-
"""
Задание 15.1b

Проверить работу функции get_ip_from_cfg из задания 15.1a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция get_ip_from_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Скопировать функцию get_ip_from_cfg из задания 15.1a и переделать ее таким образом,
чтобы в значении словаря она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.
Ключом остается имя интерфейса.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""



import re

def get_ip_from_cfg(filename):
    ''' Looks for pairs of ip and mask in file.
    Returns dictionary.

    input:
        filename - name of file
    output:
        {'FastEthernet0/1': [('10.0.1.1', '255.255.255.0'), ('10.0.3.1', '255.255.255.0')],
         'FastEthernet0/2': [('10.0.2.1', '255.255.255.0')]}
    '''
    addresses = {}
    regex_ip_mask = re.compile('address\s+(?P<address>[\d.]+)\s+(?P<mask>[\d.]+)\s+')
    regex_inf = re.compile('^interface\s+(?P<inf>\S+)\s')
    inf = ''
    with open(filename) as f:
        for line in f:
            match_inf = regex_inf.search(line)
            if match_inf:
                inf = match_inf.group('inf')
                addresses[inf]=[]
                continue
            match_ip = regex_ip_mask.search(line)
            if inf and match_ip:
                addresses[inf].append(match_ip.groups())
    # remove items with empty values
    return {k:v for k,v in addresses.items() if v}

if __name__ == '__main__':
    print(get_ip_from_cfg('config_r2.txt'))

