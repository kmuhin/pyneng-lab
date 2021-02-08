# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона, например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список, где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список IP-адресов и/или диапазонов IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только последний октет адреса.

Функция возвращает список IP-адресов.


Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""


import subprocess
import ipaddress
from task_12_3 import print_ip_table


def convert_ranges_to_ip_list(addresses):
    '''
    convert ranges of addresses to list of addresses
    return list of addresses
    '''
    result_addresses = []
    for address in addresses:
        ip_range = address.split('-')
        # not ip_range
        if len(ip_range) == 1:
            result_addresses.append(ip_range[0])
            continue
        # range
        # second part is number, not address.
        if ip_range[1].isdigit():
            prefix, _ = ip_range[0].rsplit('.',1)
            ip_range[1] = prefix+'.'+ip_range[1]
        # convert addresses to int
        ip1_int = int(ipaddress.IPv4Address(ip_range[0]))
        ip2_int = int(ipaddress.IPv4Address(ip_range[1]))
        for ip in range(ip1_int, ip2_int+1):
            result_addresses.append(str(ipaddress.IPv4Address(ip)))
    return result_addresses

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
    ''' 
    ping addresses from list
    addresses - list of ip addresses or range of addresses
    example: ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    '''
    addresses_unreachable = []
    addresses_reachable = []
    addresses_clean = convert_ranges_to_ip_list(addresses)
    for address in addresses_clean:
        if ping_ip(address):
            addresses_reachable.append(address)
        else:
            addresses_unreachable.append(address)
    return addresses_reachable, addresses_unreachable

if __name__ == '__main__':
    test_addresses = ['8.8.8.8', '1.1.1.1', 'a.a.a.a', 
            'aaa', '260.1.1.1', 'localhost',
            '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    alive, unreachable = ping_ip_addresses(test_addresses)
    print('alive: ', alive)
    print('unreachable: ', unreachable)
    print_ip_table(alive, unreachable)

