# -*- coding: utf-8 -*-
"""
Задание 20.1

Создать функцию generate_config.

Параметры функции:
* template - путь к файлу с шаблоном (например, "templates/for.txt")
* data_dict - словарь со значениями, которые надо подставить в шаблон

Функция должна возвращать строку с конфигурацией, которая была сгенерирована.

Проверить работу функции на шаблоне templates/for.txt и данных из файла data_files/for.yml.

"""
import yaml
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def read_yaml(data_file):
    """
    reads yaml file and returns data
    :param data_file:
    :return: data
    """
    try:
        f = open(data_file)
    except OSError:
        print("Could not open/read file:", data_file)
        return None
    with f:
        data = yaml.safe_load(f)
    return data


def generate_config(template_file, data_dict):
    if not Path(template_file).is_file():
        print('File not found: ', template_file)
        return None
    # get path to template file
    tmp_path = Path(template_file).parent
    # get template file name
    tmp_file = Path(template_file).name
    # first set path to templates
    env = Environment(loader=FileSystemLoader(tmp_path), trim_blocks=True, lstrip_blocks=True)
    # second load template itself
    tmp = env.get_template(tmp_file)
    # generate and return output
    return tmp.render(data_dict)

# так должен выглядеть вызов функции
if __name__ == "__main__":
    data_file = "data_files/for.yml"
    template_file = "templates/for.txt"
    with open(data_file) as f:
        data = read_yaml(data_file)
    print(generate_config(template_file, data))

