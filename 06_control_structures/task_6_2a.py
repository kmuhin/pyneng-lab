# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


input_ip = input('Введите IP-адрес в формате [10.0.1.1]: ') or '10.0.1.1'

blnIpIsCorrect = True
ip = []
# cutting input into parts separated by dot
# expecting each part is a number in range 0-255
for octet in input_ip.split('.'):
    # octet is a number
    if octet.isdigit():
        octet = int(octet)
        # the number must be in the range 0-255
        if 0 <= octet <=255:
            ip.append(octet)
        else:
            blnIpIsCorrect = False
            break
    else:
        blnIpIsCorrect = False
        break
# we need four numbers
if not blnIpIsCorrect or len(ip) != 4:
    print('Неправильный IP-адрес')
# Everything is fine. Let's continue.
else:
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

