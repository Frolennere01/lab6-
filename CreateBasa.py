import sqlite3

def create_data_basa():
    conn = sqlite3.connect('basa.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER
    );
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS e_addresses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );
    ''') #addresses с внешним ключом на users

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pet TEXT NOT NULL,
            user_id INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(id)
        );
        ''')  # pet с внешним ключом на users

    cursor.execute("INSERT INTO users (name, age) VALUES ('Николай', 30);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Виталий', 20);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Андрей', 24);")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Василий', 27);")


    cursor.execute("INSERT INTO e_addresses (email, user_id) VALUES ('andrey456@mail.com', 1);")
    cursor.execute("INSERT INTO e_addresses (email, user_id) VALUES ('tankionline@yandex.com', 2);")
    cursor.execute("INSERT INTO e_addresses (email, user_id) VALUES ('damagextra@gmail.com', 3);")
    cursor.execute("INSERT INTO e_addresses (email, user_id) VALUES ('ultrakiller3000@gmail.com', 4);")

    cursor.execute("INSERT INTO pets (pet, user_id) VALUES ('cat', 1);")
    cursor.execute("INSERT INTO pets (pet, user_id) VALUES ('cat', 2);")
    cursor.execute("INSERT INTO pets (pet, user_id) VALUES ('sparrow', 3);")
    cursor.execute("INSERT INTO pets (pet, user_id) VALUES ('dog', 4);")

    conn.commit()
    conn.close()

    print("Успех")

# Запускаем создание базы данных
create_data_basa()
