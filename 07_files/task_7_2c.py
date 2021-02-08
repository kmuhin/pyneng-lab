# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]

from sys import argv

blnHaveAllArgs = False
try:
    filename = argv[1]
    file_cleared = argv[2]
except IndexError:
    print(f'Usage: {argv[0]} oldfile newfile')
else:
    blnHaveAllArgs = True

if blnHaveAllArgs:
    with open(filename) as f:
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
                # remove new line at the end
                f_cleared.write(line)
