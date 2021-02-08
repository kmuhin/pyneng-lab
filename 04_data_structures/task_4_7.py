# -*- coding: utf-8 -*-
"""
Задание 4.7

Преобразовать MAC-адрес в строке mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

mac = "AAAA:BBBB:CCCC"

mac1, mac2, mac3 = mac.split(':')
mac_v1 = f'{int(mac1,base=16):b}{int(mac2,base=16):b}{int(mac3,base=16):b}'
print(mac_v1)

mac_hex = mac.replace(':', '')
mac_bin = bin(int(mac_hex, base=16))
mac_v2 = mac_bin[2:]
print(mac_v2)

print(mac_v1 == mac_v2)
