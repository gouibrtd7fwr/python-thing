import sqlite3
from pathlib import Path

database = Path(__file__).resolve().with_name("shop.db")
conn = sqlite3.connect(database)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username TEXT,
        name TEXT,
        password TEXT
    )
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY,
        name TEXT,
        price INTEGER
    )
    """)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_id INTEGER,
        quantity INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id)
        FOREIGN KEY (product_id) REFERENCES product(id)
    )
    """)

list_user = [
    ('maria3311@gmail.com', 'Maria22', '8883311'),
    ('johnjacks777@yahoo.com', 'John Jacks', '@john1470'),
    ('lora120392@gmail.com', 'Lora Kevin', 'lorlikesmusic!')
]

list_product = [
    ("Snippet Sharing", 5),
    ("Automatic Error Detector", 1),
    ("Feather Code", 0)
]
cursor.executemany("""
    INSERT INTO user (username, name, password)
    VALUES (?,?,?)
    """, list_user)

cursor.executemany("""
    INSERT INTO product (name, price)
    VALUES (?,?)
    """, list_product)

cursor.execute("""
   INSERT INTO cart (user_id, product_id, quantity)
   VALUES (1,1,2)
 """)
cursor.execute("""
   INSERT INTO cart (user_id, product_id, quantity)
   VALUES (1,2,2)
 """)
cursor.execute("""
   INSERT INTO cart (user_id, product_id, quantity)
   VALUES (2,1,1)
 """)
cursor.execute("""
   INSERT INTO cart (user_id, product_id, quantity)
   VALUES (2,2,4)
 """)
cursor.execute("""
   INSERT INTO cart (user_id, product_id, quantity)
   VALUES (2,3,1)
 """)


conn.commit()
cursor.execute('SELECT * FROM user')
data = cursor.fetchall()
print(data)
cursor.execute('SELECT * FROM product')
data = cursor.fetchall()
print(data)
cursor.execute('SELECT name, price FROM product')
data = cursor.fetchall()
print(data)
cursor.execute('SELECT * FROM product WHERE price > 150')
data = cursor.fetchall()
print(data)

user_id = 2
cursor.execute("""
SELECT
    product.name,
    product.price,
    cart.quantity,
    product.price * cart.quantity as total
FROM cart
JOIN product
ON cart.product_id = product.id
WHERE cart.user_id = ?
""", (user_id,))

cart_items = cursor.fetchall()
total_price = 0
for item in cart_items:
    print(
        item["name"],
        "- Price",
        item["price"],
        "- Amount",
        item["quantity"],
        "- Total",
        item["total"]
    )
    total_price += item["total"]
print("Total price:", total_price)