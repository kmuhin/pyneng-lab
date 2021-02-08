# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv

prefix = argv[1]
net, net_length = prefix.split('/')
net_length = int(net_length)
net1, net2, net3, net4 = net.split('.')
netbin = f'{int(net1):08b}{int(net2):08b}{int(net3):08b}{int(net4):08b}'
netbin = netbin[:net_length] + '0' * (32 - net_length)

net1, net2, net3, net4 = int(netbin[:8], 2), int(netbin[8:16], 2), int(netbin[16:24], 2), int(netbin[24:32], 2)
net = f'{net1}.{net2}.{net3}.{net4}'
print(f'''
Network:
{net1:<10}{net2:<10}{net3:<10}{net4:<10}
{int(net1):08b}  {int(net2):08b}  {int(net3):08b}  {int(net4):08b}
''')

bitmask = '1' * net_length + '0' * (32 - net_length)
bitmask1, bitmask2, bitmask3, bitmask4 = bitmask[:8], bitmask[8:16], bitmask[16:24], bitmask[24:32]
print(f'''
Mask:
/{net_length}
{int(bitmask1, 2):<10}{int(bitmask2, 2):<10}{int(bitmask3, 2):<10}{int(bitmask4, 2):<10}
{bitmask1}  {bitmask2}  {bitmask3}  {bitmask4}  
''')
