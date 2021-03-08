from pathlib import Path
import sqlite3
import yaml
import re

workdir = Path(__file__).parent.absolute()
db_file = workdir.joinpath('dhcp_snooping.db')
switches_info_file = workdir.joinpath('switches.yml')

files_output = ['sw1_dhcp_snooping.txt',
                'sw2_dhcp_snooping.txt',
                'sw3_dhcp_snooping.txt']


def read_yaml(yaml_file=switches_info_file):
    with open(yaml_file) as f:
        return yaml.safe_load(f)


def parse_dhcp_snooping(text: str):
    """
    Parse text with output of command "show dhcp snooping binding"

    :return: list
    """
    list_bindings = []
    regex_switch = re.compile(r'(?P<mac>\S+)\s+(?P<ip>[\d.]+)\s+\d+\s+\S+\s+(?P<vlan>\d+)\s+(?P<port>\S+)$')
    for line in text.split('\n'):
        match = regex_switch.search(line)
        # regex matched
        if match:
            # since the order of the regex groups is the same as the column order,
            # pass the regex groups as a list.
            list_bindings.append(match.groups())
    return list_bindings


def read_files_dhcp_bindings(files: list):
    """
    read multiple files with output of command "show dhcp snooping binding"

    :return: dict
    """
    dict_bindings = {}
    for file in files:
        # get switch name from file name
        dev_name, _ = file.split('_', 1)
        dict_bindings[dev_name] = []
        with open(file) as f:
            bindings = parse_dhcp_snooping(f.read())
            dict_bindings[dev_name] = bindings
    return dict_bindings


def db_insert_switch(conn, switch: list):
    query = 'insert into switches values(?, ?)'
    with conn:
        try:
            conn.execute(query, switch)
        except sqlite3.IntegrityError as e:
            print(f'При добавлении данных: {switch} Возникла ошибка: {e}')


def db_insert_bindings(conn, bindings: list):
    query = 'insert into dhcp values(?, ?, ?, ?, ?)'
    with conn:
        try:
            conn.execute(query, bindings)
        except sqlite3.IntegrityError as e:
            print(f'При добавлении данных: {bindings} Возникла ошибка: {e}')


def main():
    if not db_file.is_file():
        print('База данных не существует. Перед добавлением данных, ее надо создать')
        return

    switches_info = read_yaml()
    with open(files_output[0]) as f:
        text = f.read()
    bindings = read_files_dhcp_bindings(files_output)
    bindings_to_query = [(*v, k) for k, b in bindings.items() for v in b]

    conn = sqlite3.connect(db_file)
    print('Добавляю данные в таблицу switches...')
    for row in switches_info['switches'].items():
        db_insert_switch(conn, row)
    print('Добавляю данные в таблицу dhcp...')
    for row in bindings_to_query:
        db_insert_bindings(conn, row)

    conn.close()


if __name__ == '__main__':
    main()
