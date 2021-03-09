from sys import argv
import sqlite3
from pathlib import Path
from tabulate import tabulate

workdir = Path(__file__).parent.absolute()
db_file = workdir.parent.joinpath('task_25_1', 'dhcp_snooping.db')


def get_columns_from_cursor(cur: sqlite3.Cursor):
    return [i[0] for i in cur.description]


def db_print_all_dhcp(conn: sqlite3.Connection):
    print('В таблице dhcp такие записи:')
    query = 'select * from dhcp'
    cur = conn.execute(query)
    columns = get_columns_from_cursor(cur)
    print(tabulate(cur.fetchall(), headers=columns))


def db_print_from_dhcp(conn, param, value):
    print(f'Информация об устройствах с такими параметрами: {param} {value}')
    query = f'select * from dhcp where {param} = ?'
    cur = conn.execute(query, (value,))
    columns = get_columns_from_cursor(cur)
    print(tabulate(cur.fetchall(), headers=columns))


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
        db_print_all_dhcp(conn)
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
        db_print_from_dhcp(conn, param, value)
    else:
        # wrong number of arguments
        print('Пожалуйста, введите два или ноль аргументов')
    conn.close()


if __name__ == '__main__':
    main()
