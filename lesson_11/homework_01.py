"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id
"""

import sqlite3


def create_table(products):
    with sqlite3.connect("my_db.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name VARCHAR,
            price FLOAT,
            volume INTEGER,
            comment VARCHAR);
            """
        )
        db.commit()

def create_data(product_name: str, price: int, volume: int, comment: str):
    with sqlite3.connect("products.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(
            """INSERT INTO products (product_name, price, volume, comment)
            VALUES (?, ?, ?, ?);            
            """,
            (product_name, price, volume, comment),
        )
        db.commit()


def read_data(id_name: int = None):
    with sqlite3.connect("products.sqlite3") as db:
        cursor = db.cursor()
        if not id_name:
            cursor.execute(
                """
                SELECT * FROM products;        
                """
            )
        else:
            cursor.execute(
                """
                SELECT * FROM products WHERE id = ?;        
                """, (id_name,)
            )
    return db.fetchall()


def update_data(id_number: int, product_name: str, price: float, volume: int, comment: str):
    with sqlite3.connect("products.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(
            """UPDATE products
                SET product_name=?, price=?, volume=?, comment=?
                WHERE id = ?;            
            """,
            (product_name, price, volume, comment, id_number)
        )
        db.commit()


def delete_data(id_number: int):
    with sqlite3.connect("products.sqlite3") as db:
        cursor = db.cursor()
        cursor.execute(
            """
            DELETE FROM products WHERE id = ?;            
            """,
            (id_number,)
        )
        db.commit()


