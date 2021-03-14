from pathlib import Path
import sqlite3
import yaml
import re

workdir = Path(__file__).parent.absolute()
db_file = workdir.joinpath('dhcp_snooping.db')
newdatadir = workdir.joinpath('new_data')
switches_info_file = workdir.joinpath('switches.yml')

files_output = ['sw1_dhcp_snooping.txt',
                'sw2_dhcp_snooping.txt',
                'sw3_dhcp_snooping.txt'
                ]

files_output_2 = [newdatadir.joinpath(i) for i in files_output]


def read_yaml(yaml_file):
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
        file = Path(file)
        if not file.is_absolute():
            file = workdir.joinpath(file)
        if not file.is_file():
            print(f'Нет такого файла: {file}')
            continue
        dev_name, _ = file.name.split('_', 1)
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


def db_update_bindings_inactive(conn):
    query = 'update dhcp set active=0'
    with conn:
        conn.execute(query)


def db_insert_dhcp(conn, bindings_row: list):
    query = 'insert into dhcp values(?, ?, ?, ?, ?, 1)'
    with conn:
        try:
            conn.execute(query, bindings_row)
        except sqlite3.IntegrityError as e:
            print(f'При добавлении данных: {bindings_row} Возникла ошибка: {e}')


def db_replace_dhcp(conn, bindings_row: list):
    query = 'replace into dhcp values(?, ?, ?, ?, ?, 1)'
    with conn:
        conn.execute(query, bindings_row)


def db_update_dhcp(conn, bindings_row: list):
    query = f'update dhcp set ip=?, vlan=?, interface=?, switch=?, active=1 where mac="{bindings_row[0]}"'
    with conn:
        conn.execute(query, bindings_row[1:])


def make_bindings_to_query(bindings: dict):
    return [(*v, k) for k, b in bindings.items() for v in b]


def db_insert_bindings(conn, bindings: dict):
    db_update_bindings_inactive(conn)
    bindings_to_query = make_bindings_to_query(bindings)
    for row in bindings_to_query:
        print(row)
        # db_insert_dhcp(conn, row)
        # db_update_dhcp(conn, row)
        # alternative of two operations - sql replace
        db_replace_dhcp(conn, row)


def main():
    if not db_file.is_file():
        print('База данных не существует. Перед добавлением данных, ее надо создать')
        return

    switches_info = read_yaml(switches_info_file)

    conn = sqlite3.connect(db_file)
    print('Добавляю данные в таблицу switches...')
    for row in switches_info['switches'].items():
        db_insert_switch(conn, row)
    print('Добавляю данные в таблицу dhcp...')
    # first piece of data
    bindings = read_files_dhcp_bindings(files_output)
    db_insert_bindings(conn, bindings)
    # second piece of data
    bindings = read_files_dhcp_bindings(files_output_2)
    db_insert_bindings(conn, bindings)

    conn.close()


if __name__ == '__main__':
    main()
