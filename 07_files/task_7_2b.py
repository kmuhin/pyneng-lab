# -*- coding: utf-8 -*-
"""
Задание 7.2b

Дополнить скрипт из задания 7.2a:
* вместо вывода на стандартный поток вывода,
  скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore.
Строки, которые начинаются на '!' отфильтровывать не нужно.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

file_cleared = 'config_sw1_cleared.txt'

# expecting one argument
if len(argv) > 1:
    with open(argv[1]) as f:
        with open(file_cleared, 'w') as f_cleared:
            for line in f:
                blnIgnore = False
                # ingnore lines with words from list ignore
                for ign in ignore:
                    if ign in line:
                        blnIgnore = True
                        break
                if blnIgnore:
                    continue
                # write to new file. there is no new line(\n) needed because line already ontains it.
                f_cleared.write(line)
