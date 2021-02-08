# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


prefix = input('Введите IP-сеть в формате: 10.1.1.0/24: ') or '10.1.1.0/24'
print(f'\nPrefix: {prefix}')
net, net_length = prefix.split('/')
net1, net2, net3, net4 = net.split('.')
print(f'''
Network:
{net1:10}{net2:10}{net3:10}{net4:10}
{int(net1):08b}  {int(net2):08b}  {int(net3):08b}  {int(net4):08b}
''')

net_length = int(net_length)
bitmask = '1'*net_length + '0'*(32-net_length)
bitmask1, bitmask2, bitmask3, bitmask4 = bitmask[:8], bitmask[8:16], bitmask[16:24], bitmask[24:32]
print(f'''
Mask:
/{net_length}
{int(bitmask1,2):<10}{int(bitmask2,2):<10}{int(bitmask3,2):<10}{int(bitmask4,2):<10}
{bitmask1}  {bitmask2}  {bitmask3}  {bitmask4}  
''')

