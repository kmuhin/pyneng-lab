# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""

import re

def get_ip_from_cfg(filename):
    ''' Looks for pairs of ip and mask in file.
    Returns dictionary where key is interface and value is pair of ip and mac.

    input:
        filename - name of file
    output:
        {'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
         'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}
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
                continue
            match_ip = regex_ip_mask.search(line)
            if inf and match_ip:
                addresses[inf] = (match_ip.groups())
    return addresses

if __name__ == '__main__':
    print(get_ip_from_cfg('config_r1.txt'))

