# -*- coding: utf-8 -*-
"""
Задание 17.3b

Создать функцию transform_topology, которая преобразует топологию в формат подходящий для функции draw_topology.

Функция ожидает как аргумент имя файла в формате YAML, в котором хранится топология.

Функция должна считать данные из YAML файла, преобразовать их соответственно, чтобы функция возвращала словарь такого вида:
    {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
     ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

Функция transform_topology должна не только менять формат представления топологии, но и удалять дублирующиеся соединения (их лучше всего видно на схеме, которую генерирует функция draw_topology из файла draw_network_graph.py).

Проверить работу функции на файле topology.yaml (должен быть создан в задании 17.3a).
На основании полученного словаря надо сгенерировать изображение топологии с помощью функции draw_topology.
Не копировать код функции draw_topology из файла draw_network_graph.py.

Результат должен выглядеть так же, как схема в файле task_17_3b_topology.svg

При этом:
* Интерфейсы должны быть записаны с пробелом Fa 0/0
* Расположение устройств на схеме может быть другим
* Соединения должны соответствовать схеме
* На схеме не должно быть дублирующихся линков


> Для выполнения этого задания, должен быть установлен graphviz:
> apt-get install graphviz

> И модуль python для работы с graphviz:
> pip install graphviz

"""

import yaml
from draw_network_graph import draw_topology


def transform_topology(topology_yaml):
    """
    making topology from yaml file to function draw_topology

    func returns dict withou duplicates like:
        {('R4', 'Fa 0/1'): ('R5', 'Fa 0/1'),
         ('R4', 'Fa 0/2'): ('R6', 'Fa 0/0')}

    :param topology_yaml - yaml file name with topology, example was made in task 17.3a
    :return dict
    """
    templates = ''
    dict_topology = {}
    with open(topology_yaml) as f:
        templates = yaml.safe_load(f)
    for dev_local, v0 in templates.items():
        for inf_local, v1 in v0.items():
            dev_remote, inf_remote = tuple(*v1.items())
            for dev in dict_topology.items():
                if set(dev) == set(((dev_local, inf_local), (dev_remote, inf_remote))):
                    break
            else:
                dict_topology[dev_local, inf_local] = dev_remote, inf_remote
    return dict_topology


if __name__ == '__main__':
    topology = transform_topology('topology.yaml')
    print(len(topology))
    for k, v in topology.items():
        print(k, v)
    draw_topology(topology)
    draw_topology(topology)