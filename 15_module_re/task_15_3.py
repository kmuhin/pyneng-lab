# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""

import re

def convert_ios_nat_to_asa(filename_ios, filename_asa):
    '''
    Converting file with IOS NAT rules to file with ASA NAT rules
    
    input:
        filename_ios - name of file with IOS NAT rules
        filename_asa - name of file for writing with ASA NAT rules
    no output
    
    '''
    template_asa = [ 'object network LOCAL_{ip}',
            ' host {ip}',
            ' nat (inside,outside) static interface service {proto} {port_local} {port_public}']
    regex_ios = re.compile(r' +(?P<proto>\w+) +'
                            r'(?P<ip>[\d.]+) +'
                            r'(?P<port_local>\d{1,5}) +\w+ +\S+ +'
                            r'(?P<port_public>\d{1,5})$')
    print(regex_ios.pattern)
    with open(filename_ios) as f:
        with open(filename_asa,'w') as f_asa:
            for line in f:
                print(line)
                match = regex_ios.search(line)
                if match:
                    print(match.groups())
                    rule_asa = '\n'.join(template_asa).format(**match.groupdict())
                    f_asa.write(rule_asa+'\n')


if __name__ == '__main__':
    convert_ios_nat_to_asa('cisco_nat_config.txt', 'cisco_nat_config_asa.txt')

