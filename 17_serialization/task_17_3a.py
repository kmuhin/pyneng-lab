# -*- coding: utf-8 -*-
"""
Задание 17.3a

Создать функцию generate_topology_from_cdp, которая обрабатывает вывод команды show cdp neighbor из нескольких файлов и записывает итоговую топологию в один словарь.

Функция generate_topology_from_cdp должна быть создана с параметрами:
* list_of_files - список файлов из которых надо считать вывод команды sh cdp neighbor
* save_to_filename - имя файла в формате YAML, в который сохранится топология.
 * значение по умолчанию - None. По умолчанию, топология не сохраняется в файл
 * топология сохраняется только, если save_to_filename как аргумент указано имя файла

Функция должна возвращать словарь, который описывает соединения между устройствами, независимо от того сохраняется ли топология в файл.

Структура словаря должна быть такой:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}},
 'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
 'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.

Проверить работу функции generate_topology_from_cdp на списке файлов:
* sh_cdp_n_sw1.txt
* sh_cdp_n_r1.txt
* sh_cdp_n_r2.txt
* sh_cdp_n_r3.txt
* sh_cdp_n_r4.txt
* sh_cdp_n_r5.txt
* sh_cdp_n_r6.txt

Проверить работу параметра save_to_filename и записать итоговый словарь в файл topology.yaml.

"""

import yaml
from task_17_3 import parse_sh_cdp_neighbors


def generate_topology_from_cdp(list_of_files, save_to_filename=None):
    """
    parsing command output 'show cdp neighbor' from files
    writing result to yaml file if file_yaml is specified
    return dict like:
        {'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
                'Fa 0/2': {'R6': 'Fa 0/0'}},
         'R5': {'Fa 0/1': {'R4': 'Fa 0/1'}},
         'R6': {'Fa 0/0': {'R4': 'Fa 0/2'}}}

    :param list_of_files - list of files
    :param save_to_filename - yaml file to save result
    :return dict
    """
    print(list_of_files)
    dict_cdp = {}
    for file_cdp in list_of_files:
        with open(file_cdp) as f:
            dict_cdp.update(parse_sh_cdp_neighbors(f.read()))
    if save_to_filename:
        with open(save_to_filename, 'w') as f:
            yaml.dump(dict_cdp, f, default_flow_style=False)
    return dict_cdp


if __name__ == '__main__':
    list_of_cdp_files = [
        "sh_cdp_n_r2.txt",
        "sh_cdp_n_r5.txt",
        "sh_cdp_n_r1.txt",
        "sh_cdp_n_sw1.txt",
        "sh_cdp_n_r3.txt",
        "sh_cdp_n_r4.txt",
        "sh_cdp_n_r6.txt",
    ]
    print(generate_topology_from_cdp(list_of_cdp_files, 'topology.yaml'))
