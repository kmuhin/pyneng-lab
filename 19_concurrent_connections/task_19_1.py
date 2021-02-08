# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""

from concurrent.futures import ThreadPoolExecutor
import ipaddress
import platform
import subprocess
import logging

logging.basicConfig(level=logging.INFO)


def ping_ip(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        logging.info(f'incorrect ip: {ip}')
        return False
    if 'Windows' in platform.system():
        args = ['ping', '-w', '500', '-n', '1', ip]
    else:
        args = ['ping', '-w1', '-nc1', ip]
    result = subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    logging.info(f'command: {" ".join(args)}')
    return True if result.returncode == 0 else False


def ping_ip_addresses(ip_list, limit=3):
    list_unreachable = []
    list_reachable = []
    with ThreadPoolExecutor(max_workers=limit) as executor:
        result = executor.map(ping_ip, ip_list)
        for ip, status in zip(ip_list, result):
            if status:
                list_reachable.append(ip)
            else:
                list_unreachable.append(ip)
    return list_reachable, list_unreachable


if __name__ == '__main__':
    addresses = ['8.8.8.8', '10.0.1.2', '2.2.2.2', '127.0.0.1', 'ya.ru']
    print(ping_ip_addresses(addresses))
