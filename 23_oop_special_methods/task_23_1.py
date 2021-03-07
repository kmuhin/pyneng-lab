# -*- coding: utf-8 -*-

"""
Задание 23.1

В этом задании необходимо создать класс IPAddress.

При создании экземпляра класса, как аргумент передается IP-адрес и маска,
а также должна выполняться проверка корректности адреса и маски:
* Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255
* маска считается корректной, если это число в диапазоне от 8 до 32 включительно

Если маска или адрес не прошли проверку, необходимо сгенерировать
исключение ValueError с соответствующим текстом (вывод ниже).

Также, при создании класса, должны быть созданы два атрибута экземпляра:
ip и mask, в которых содержатся адрес и маска, соответственно.

Пример создания экземпляра класса:
In [1]: ip = IPAddress('10.1.1.1/24')

Атрибуты ip и mask
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24

Проверка корректности адреса (traceback сокращен)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Проверка корректности маски (traceback сокращен)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

"""


class IPAddress:
    def __init__(self, ipaddress):
        t_ip, t_mask = ipaddress.split('/')
        self.ip = self._check_ip(t_ip)
        self.mask = self._check_mask(t_mask)

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
