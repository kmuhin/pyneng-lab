from pathlib import Path
import sqlite3

workdir = Path(__file__).parent.absolute()
db_file = workdir.joinpath('dhcp_snooping.db')
db_schema_file = workdir.joinpath('dhcp_snooping_schema.sql')


def create_db(rewrite=False):
    if db_file.is_file():
        if rewrite:
            db_file.unlink()
        else:
            print('База данных существует')
            return
    print('Создаю базу данных...')
    conn = sqlite3.connect(db_file)
    with open(db_schema_file) as f:
        db_schema = f.read()
    with conn:
        conn.executescript(db_schema)

    conn.close()


if __name__ == '__main__':
    create_db()
