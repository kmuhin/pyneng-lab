# -*- coding: utf-8 -*-
"""
Задание 9.4

Создать функцию convert_config_to_dict, которая обрабатывает конфигурационный файл коммутатора и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ignore = ["duplex", "alias", "Current configuration"]


def ignore_command(command, ignore):
    """
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    """
    return any(word in command for word in ignore)

def convert_config_to_dict(config_filename:str)->dict:
    '''
    Функция конвертирует текстовый конфиг из файла в словарь.

    config_filename - имя файла
    
    Возвращает словарь:
    * Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
    * Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки надо удалить).
    * Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком
    '''
    dict_config = {}
    g_cmd = ''
    with open(config_filename) as f:
        for line in f:
            # skip blank lines
            if not line.strip():
                continue
            # skip comments and ignore words
            if line.startswith('!') or ignore_command(line, ignore):
                continue
            # subcommand follows indentation
            if line.startswith(' '):
                if g_cmd:
                    dict_config[g_cmd].append(line.strip())
            # command finally
            else:
                g_cmd = line.strip()
                dict_config[g_cmd] = []

    return dict_config


if __name__ == '__main__':
    dict_config = convert_config_to_dict('config_sw1.txt')
    print(dict_config)
