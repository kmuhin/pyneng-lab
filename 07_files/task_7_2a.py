# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]


from sys import argv

# expecting one argument
if len(argv) > 1:
    with open(argv[1]) as f:
        for line in f:
            blnIgnore = False
            # skip comments starting with '!' and blank lines
            if line.startswith('!') or not line.strip():
                continue
            # ingnore lines with words from list ignore
            for ign in ignore:
                if ign in line:
                    blnIgnore = True
                    break
            if blnIgnore:
                continue
            # remove new line at the end
            print(line.rstrip())
