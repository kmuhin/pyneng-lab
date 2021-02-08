# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


with open('ospf.txt') as f:
    for line in f:
        print(line)
        route = line.replace(',','').split()
        print(f'''\
{'Prefix':22}{route[1]}
{'AD/Metric':22}{route[2]}
{'Next-Hop':22}{route[4]}
{'Last update':22}{route[5]}
{'Outbound Interface':22}{route[6]} 
''')

