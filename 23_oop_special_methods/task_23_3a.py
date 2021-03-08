# -*- coding: utf-8 -*-

"""
Задание 23.3a

В этом задании надо сделать так, чтобы экземпляры класса Topology
были итерируемыми объектами.
Основу класса Topology можно взять из любого задания 22.1x или задания 23.3.

После создания экземпляра класса, экземпляр должен работать как итерируемый объект.
На каждой итерации должен возвращаться кортеж, который описывает одно соединение.
Порядок вывода соединений может быть любым.


Пример работы класса:

In [1]: top = Topology(topology_example)

In [2]: for link in top:
   ...:     print(link)
   ...:
(('R1', 'Eth0/0'), ('SW1', 'Eth0/1'))
(('R2', 'Eth0/0'), ('SW1', 'Eth0/2'))
(('R2', 'Eth0/1'), ('SW2', 'Eth0/11'))
(('R3', 'Eth0/0'), ('SW1', 'Eth0/3'))
(('R3', 'Eth0/1'), ('R4', 'Eth0/0'))
(('R3', 'Eth0/2'), ('R5', 'Eth0/0'))


Проверить работу класса.
"""

topology_example = {
    ("R1", "Eth0/0"): ("SW1", "Eth0/1"),
    ("R2", "Eth0/0"): ("SW1", "Eth0/2"),
    ("R2", "Eth0/1"): ("SW2", "Eth0/11"),
    ("R3", "Eth0/0"): ("SW1", "Eth0/3"),
    ("R3", "Eth0/1"): ("R4", "Eth0/0"),
    ("R3", "Eth0/2"): ("R5", "Eth0/0"),
    ("SW1", "Eth0/1"): ("R1", "Eth0/0"),
    ("SW1", "Eth0/2"): ("R2", "Eth0/0"),
    ("SW1", "Eth0/3"): ("R3", "Eth0/0"),
}


class Topology:
    def __init__(self, topology_dict):
        self.topology = self._normalize(topology_dict)

    def __iter__(self):
        return iter(self.topology.items())

    def __add__(self, other):
        toponew = type(self)(self.topology)
        for link in other.topology.items():
            toponew.add_link(*link)
        return toponew


    def _normalize(self, topology):
        dev_filtered = {}
        for link in topology.items():
            for filtered in dev_filtered.items():
                if set(link) == set(filtered):
                    break
            else:
                dev_filtered[link[0]] = link[1]
        return dev_filtered

    def delete_link(self, if1, if2):
        for link in self.topology.items():
            if set(link) == set((if1, if2)):
                del self.topology[link[0]]
                break
        else:
            print('Такого соединения нет')

    def delete_node(self, device):
        found = False
        for link in dict(self.topology).items():
            if device in (link[0][0], link[1][0]):
                del self.topology[link[0]]
                found = True
        if not found:
            print('Такого устройства нет')

    def add_link(self, if1, if2):
        link_new = if1, if2
        for link in self.topology.items():
            # all elements of link_new are in the link
            if set(link) == set(link_new):
                print('Такое соединение существует')
                return
            # some elements of link_new are in the link
            elif not set(link).isdisjoint(link_new):
                print('Cоединение с одним из портов существует')
                return
        # there are no link_new in the topology dict so add it to dict
        self.topology[if1] = if2

if __name__ == '__main__':
    t1 = Topology(topology_example)

