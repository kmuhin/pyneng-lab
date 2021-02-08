# -*- coding: utf-8 -*-
"""
Задание 17.1

Создать функцию write_dhcp_snooping_to_csv, которая обрабатывает
вывод команды show dhcp snooping binding из разных файлов и записывает обработанные данные в csv файл.

Аргументы функции:
* filenames - список с именами файлов с выводом show dhcp snooping binding
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Например, если как аргумент был передан список с одним файлом sw3_dhcp_snooping.txt:
MacAddress          IpAddress        Lease(sec)  Type           VLAN  Interface
------------------  ---------------  ----------  -------------  ----  --------------------
00:E9:BC:3F:A6:50   100.1.1.6        76260       dhcp-snooping   3    FastEthernet0/20
00:E9:22:11:A6:50   100.1.1.7        76260       dhcp-snooping   3    FastEthernet0/21
Total number of bindings: 2

В итоговом csv файле должно быть такое содержимое:
switch,mac,ip,vlan,interface
sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21


Проверить работу функции на содержимом файлов sw1_dhcp_snooping.txt, sw2_dhcp_snooping.txt, sw3_dhcp_snooping.txt.
Первый столбец в csv файле имя коммутатора надо получить из имени файла, остальные - из содержимого в файлах.

"""

import csv
import re


def write_dhcp_snooping_to_csv(filenames=None, output=''):
    """
    Parse the files with the output of the command "show dhcp snooping binding" and save to one csv file.

    sample of csv content:
        switch,mac,ip,vlan,interface
        sw3,00:E9:BC:3F:A6:50,100.1.1.6,3,FastEthernet0/20
        sw3,00:E9:22:11:A6:50,100.1.1.7,3,FastEthernet0/21

    :param filenames: list of file names
    :param output: csv file name
    :return: None
    """
    if not filenames or not output:
        return
    csv_header = ['switch', 'mac', 'ip', 'vlan', 'interface']
    regex_switch = re.compile(r'(?P<mac>\S+)\s+(?P<ip>[\d.]+)\s+\d+\s+\S+\s+(?P<vlan>\d+)\s+(?P<port>\S+)$')
    # csv file to output
    with open(output, 'w') as f_output:
        # csv writer
        writer = csv.writer(f_output)
        # write header
        writer.writerow(csv_header)
        # read files with output of command "show dhcp snooping binding"
        for filename in filenames:
            # switch name from file name
            switch, _ = filename.split('_', 1)
            with open(filename) as f_switch:
                for line in f_switch:
                    match = regex_switch.search(line)
                    # regex matched
                    if match:
                        # since the order of the regex groups is the same as the column order,
                        # pass the regex groups as a list.
                        writer.writerow([switch]+list(match.groups()))


if __name__ == '__main__':
    write_dhcp_snooping_to_csv(['sw1_dhcp_snooping.txt', 'sw2_dhcp_snooping.txt', 'sw3_dhcp_snooping.txt'],
                               'switches_dhcp_snooping.csv')
