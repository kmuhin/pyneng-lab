# -*- coding: utf-8 -*-
"""
Задание 7.2

Создать скрипт, который будет обрабатывать конфигурационный файл config_sw1.txt:
- имя файла передается как аргумент скрипту

Скрипт должен возвращать на стандартный поток вывода команды из переданного
конфигурационного файла, исключая строки, которые начинаются с '!'.

Вывод должен быть без пустых строк.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


from sys import argv

# expecting one argument
if len(argv) > 1:
    with open(argv[1]) as f:
        for line in f:
            # skip comments starting with '!' and blank lines
            if line.startswith('!') or not line.strip():
                continue
            # remove new line at the end
            print(line.rstrip())
else:
    print('File name param is needed')

