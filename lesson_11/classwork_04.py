"""
Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей
"""


import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()

if __name__=="__main__":
    create_user("Alexander", "Chaika", "manti.by@gmail.com", "TestPass1", 36)
    create_user("Dima", "Goose", "manti.by+2@gmail.com", "TestPass2", 32)
    create_user("Jack", "Smith", "manti.by+3@gmail.com", "TestPass3", 31)
    create_user("Alex", "Guadino", "manti.by+4@gmail.com", "TestPass4", 32)
    create_user("Sava", "Krasava", "manti.by+5@gmail.com", "TestPass5", 99)