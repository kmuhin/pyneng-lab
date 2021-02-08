# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


file_cam = 'CAM_table.txt'
list_cam = []

input_vlan = input('Enter vlan [100]: ') or '100'
with open(file_cam) as f_cam:
    for line in f_cam:
        cam = line.split()
        # need only lines with mac.
        # it has four columns.
        # first column is vlan.
        # filter vlan by input
        if len(cam) !=4:
            continue
        if not cam[0].isdigit() or cam[0] != input_vlan:
            continue
        # convert str vlan into int to sort
        cam[0] = int(cam[0])
        list_cam.append(cam)

for cam in sorted(list_cam):
    print(f'{cam[0]:<7}{cam[1]:17}{cam[3]}')
