from sys import argv
import sqlite3
from pathlib import Path
from tabulate import tabulate

workdir = Path(__file__).parent.absolute()
db_file = workdir.parent.joinpath('task_25_3', 'dhcp_snooping.db')


def get_columns_from_cursor(cur: sqlite3.Cursor):
    return [i[0] for i in cur.description]


def db_get_from_dhcp(conn, params: dict = None) -> sqlite3.Cursor:
    """
    Makes select in the dhcp table. Supports conditions through a dictionary.
    Returns sqlite3.Cursor.
    """
    params = params if params else {}
    parameters = []
    for par in params.keys():
        parameters.append(f'{par} = :{par}')
    query = f'select * from dhcp'
    if parameters:
        query += f' where {" and ".join(parameters)}'
    cur = conn.execute(query, params)
    return cur


def db_print_dhcp_by_active(conn: sqlite3.Connection, params: dict = None):
    params = params if params else {}
    if params:
        print(f'Информация об устройствах с такими параметрами: {params}\n')
    else:
        print('В таблице dhcp такие записи:\n')
    params.update({'active': '1'})
    cur = db_get_from_dhcp(conn, params)
    data = list(cur)
    if data:
        columns = get_columns_from_cursor(cur)
        print('Активные записи:')
        print(tabulate(data, headers=columns), '\n')
    params.update({'active': '0'})
    cur = db_get_from_dhcp(conn, params)
    data = list(cur)
    if data:
        columns = get_columns_from_cursor(cur)
        print('Неактивные записи:')
        print(tabulate(data, headers=columns))


def main():
    if not db_file.is_file():
        print('База данных не существует. Перед добавлением данных, ее надо создать')
        return
    conn = sqlite3.connect(db_file)
    # get column names
    cur = conn.execute('select * from dhcp limit 1')
    columns = get_columns_from_cursor(cur)

    if len(argv) == 1:
        # passed no arguments, so print all data
        db_print_dhcp_by_active(conn)
    elif len(argv) == 3:
        # passed two arguments: param, value
        param = argv[1]
        value = argv[2]
        # check param matches tables columns
        if param not in columns:
            print('Данный параметр не поддерживается.\n'
                  f'Допустимые значения параметров: {columns}')
            return
        # print data with filter by param = value
        db_print_dhcp_by_active(conn, {param: value})
    else:
        # wrong number of arguments
        print('Пожалуйста, введите два или ноль аргументов')
    conn.close()


if __name__ == '__main__':
    main()
