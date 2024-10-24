# Через терминал установить библиотеку для графов: pip install graphviz

import sqlite3
from graphviz import Digraph


def create_er_model(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    dot = Digraph(comment='ER Model')# Инициализация графа

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]

        dot.node(table_name, table_name) #добавляем узлы, т.е. таблицы

        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()

        cursor.execute(f"PRAGMA foreign_key_list({table_name});")
        foreign_keys = cursor.fetchall() #внешние ключи таблицы

        for fk in foreign_keys:
            referenced_table = fk[2]
            dot.edge(referenced_table, table_name, label=f'FK: {fk[3]} -> {fk[4]}')

    conn.close()

    dot.render("er_model", format="jpg")
    print("Модель создана!")

create_er_model('basa.db')
