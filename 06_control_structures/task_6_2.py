# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


input_ip = input('Введите IP-адреса в формате [10.0.1.1]: ') or '10.0.1.1'

ip = []
for octet in input_ip.split('.'):
   ip.append(int(octet)) 

print(ip)
if ip[0] > 0 and ip[0] < 224:
    print('unicast')
elif ip[0] > 223 and ip[0] < 240:
    print('multicast')
elif ip.count(255) == 4:
    print('local_broadcast')
elif ip.count(0) == 4:
    print('unassigned')
else:
    print('unused')


