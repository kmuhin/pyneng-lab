# -*- coding: utf-8 -*-
"""
Задание 15.1

Создать функцию get_ip_from_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

"""

import re


def get_ip_from_cfg(filename):
    ''' looks for pairs of ip and mask in file.
    returns list of pairs.
    input:
        filename - name of file
    output:
        [('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]
    '''
    addresses = []
    regex = re.compile('address\s+(?P<address>[\d.]+)\s+(?P<mask>[\d.]+)\s+')
    print('regex: ', regex)
    with open(filename) as f:
        for line in f:
            if 'address' in line.lower():
                print()
                print('line: ', line, end='')
                match = regex.search(line)
                if match:
                    print('match: ', match)
                    print('match.groups(): ', match.groups())
                    print('match.groupdict(): ', match.groupdict())
                    print('match.group("address"): ', match.group('address'))
                    print('match.group("mask"): ', match.group('mask'))
                    print('match.lastgroup: ', match.lastgroup)
                    addresses.append(match.groups())
                else:
                    print('no matches')
    return addresses


if __name__ == '__main__':
    addresses = get_ip_from_cfg('config_r1.txt')
    print('result:')
    print(addresses)
