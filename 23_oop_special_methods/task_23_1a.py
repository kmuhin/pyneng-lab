# -*- coding: utf-8 -*-

"""
Задание 23.1a

Скопировать и изменить класс IPAddress из задания 23.1.

Добавить два строковых представления для экземпляров класса IPAddress.
Как дожны выглядеть строковые представления, надо определить из вывода ниже:

Создание экземпляра
In [5]: ip1 = IPAddress('10.1.1.1/24')

In [6]: str(ip1)
Out[6]: 'IP address 10.1.1.1/24'

In [7]: print(ip1)
IP address 10.1.1.1/24

In [8]: ip1
Out[8]: IPAddress('10.1.1.1/24')

In [9]: ip_list = []

In [10]: ip_list.append(ip1)

In [11]: ip_list
Out[11]: [IPAddress('10.1.1.1/24')]

In [12]: print(ip_list)
[IPAddress('10.1.1.1/24')]

"""


class IPAddress:
    def __init__(self, ipaddress):
        t_ip, t_mask = ipaddress.split('/')
        self.ip = self._check_ip(t_ip)
        self.mask = self._check_mask(t_mask)

    def __repr__(self):
        return f'{type(self).__name__}(\'{self.ip}/{self.mask}\')'

    def __str__(self):
        return f'IP address {self.ip}/{self.mask}'

    def _check_ip(self, t_ip):
        octets = t_ip.split('.')
        is_ip_correct = True
        if len(octets) != 4:
            is_ip_correct = False
        else:
            for octet in octets:
                # octet is a number
                if octet.isdigit():
                    octet = int(octet)
                    if 0 > octet or octet > 255:
                        is_ip_correct = False
                        break
                else:
                    is_ip_correct = False
                    break
        if not is_ip_correct:
            raise ValueError('Incorrect IPv4 address')
        return t_ip

    def _check_mask(self, t_mask):
        is_mask_correct = True
        if not t_mask:
            is_mask_correct = False
        else:
            if not t_mask.isdigit():
                is_mask_correct = False
            else:
                t_mask = int(t_mask)
                if 32 < t_mask or t_mask < 8:
                    is_mask_correct = False

        if not is_mask_correct:
            raise ValueError('Incorrect mask')
        return t_mask
