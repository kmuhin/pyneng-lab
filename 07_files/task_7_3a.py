# -*- coding: utf-8 -*-
"""
Задание 7.3a

Сделать копию скрипта задания 7.3.

Дополнить скрипт:
- Отсортировать вывод по номеру VLAN

В результате должен получиться такой вывод:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Обратите внимание на vlan 1000 - он должен выводиться последним.
Правильной сортировки можно добиться, если vlan будет числом, а не строкой.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

file_cam = 'CAM_table.txt'
list_cam = []

with open(file_cam) as f_cam:
    for line in f_cam:
        cam = line.split()
        # need only lines with mac.
        # it has four columns.
        # first column is vlan.
        if len(cam) !=4:
            continue
        if not cam[0].isdigit():
            continue
        # convert str vlan into int to sort
        cam[0] = int(cam[0])
        list_cam.append(cam)

for cam in sorted(list_cam):
    print(f'{cam[0]:<7}{cam[1]:17}{cam[3]}')
