# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


import subprocess
import ipaddress
from pprint import pprint

def ping_ip(address):
    try:
        ipaddress.ip_address(address)
    except ValueError:
        return False
    result = subprocess.run(['ping', '-w1', '-nc1', address], 
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)
    return True if result.returncode == 0 else False

def ping_ip_addresses(addresses):
    addresses_unreachable = []
    addresses_reachable = []
    for address in addresses:
        if ping_ip(address):
            addresses_reachable.append(address)
        else:
            addresses_unreachable.append(address)
    return addresses_reachable, addresses_unreachable

if __name__ == '__main__':
    test_addresses = ['8.8.8.8', '1.1.1.1', 'a.a.a.a', 'aaa', '260.1.1.1', 'localhost', '']
    alive, unreachable = ping_ip_addresses(test_addresses)
    print('alive: ', alive)
    print('unreachable: ', unreachable)

