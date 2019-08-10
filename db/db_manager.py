import psycopg2
import json

DB_CONFIG_NAME = "db_config.json"

conn = None


def init():
    global conn
    with open(DB_CONFIG_NAME, "r") as file:
        json_str = file.read()
        if json_str:
            config = json.loads(json_str)
            conn = psycopg2.connect(database=config['database'],
                                    user=config['user'],
                                    password=config['password'],
                                    host=config['host'],
                                    port=config['port'])


# 是否已经初始化了
def is_init():
    return conn is not None


def do(closure):
    if conn:
        cursor = conn.cursor()
        closure(cursor)
        conn.commit()


def query(sql_closure, handle_closure):
    if conn:
        cursor = conn.cursor
        sql_closure(cursor)
        rows = cursor.fetchall()
        handle_closure(rows)


def release():
    conn.close()
