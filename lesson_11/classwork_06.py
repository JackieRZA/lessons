"""
Создать функцию для поиска всех пользователей в возрасте от X до Y лет.
"""

import sqlite3


def select_user(from_age: str, to_age: str):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age => ? AND age <= ?;
            """,
            (name,)
        )
        session.commit()
        return cursor.fetchall()


if __name__ == "__main__":
    print(select_user("23, 40"))
