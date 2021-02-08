# -*- coding: utf-8 -*-
"""
Задание 15.4

Создать функцию get_ints_without_description, которая ожидает как аргумент
имя файла, в котором находится конфигурация устройства.


Функция должна обрабатывать конфигурацию и возвращать список имен интерфейсов,
на которых нет описания (команды description).

Пример интерфейса с описанием:
interface Ethernet0/2
 description To P_r9 Ethernet0/2
 ip address 10.0.19.1 255.255.255.0
 mpls traffic-eng tunnels
 ip rsvp bandwidth

Интерфейс без описания:
interface Loopback0
 ip address 10.1.1.1 255.255.255.255

Проверить работу функции на примере файла config_r1.txt.
"""


import re

def get_ints_without_description(filename):
    '''
    the function looks for interfaces without a description in the config file

    input
        filename - name of config file
    output
        list of interfaces:
            ["Loopback0", "Tunnel0", "Ethernet0/1",]

    '''
    interfaces = []
    inf = ''
    descr = ''
    regexp = re.compile(r'^interface +(?P<inf>\S+$)'
                        r'| description +(?P<descr>.+$)')
    with open(filename) as f:
        for line in f:
            # if line starts with comment literal '!'
            if line.startswith('!'):
                # if we have both interface and description just reset variables
                if inf and descr:
                    inf = descr = ''
                    continue
                # if we have only interface save to list
                if inf:
                    interfaces.append(inf)
                    inf = ''
                continue
            match = regexp.search(line)
            if match:
                # found interface
                if match.lastgroup == 'inf':
                    inf = match.group(match.lastgroup)
                    continue
                # found desctiption
                if match.lastgroup == 'descr':
                    descr =  match.group(match.lastgroup)
    return interfaces


if __name__ == '__main__':
    print(get_ints_without_description('config_r1.txt'))

