import sqlite3
import random

class ElectronicStore:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS products (
            product_id INTEGER PRIMARY KEY,
            product_name TEXT NOT NULL,
            price REAL NOT NULL
        )
        """
        self.conn.execute(query)
        self.conn.commit()

    def insert_product(self, product_name, price):
        query = "INSERT INTO products (product_name, price) VALUES (?, ?)"
        self.conn.execute(query, (product_name, price))
        self.conn.commit()

    def update_product(self, product_id, product_name=None, price=None):
        query = "UPDATE products SET "
        params = []
        if product_name is not None:
            query += "product_name = ?, "
            params.append(product_name)
        if price is not None:
            query += "price = ?, "
            params.append(price)
        query = query.rstrip(", ") + " WHERE product_id = ?"
        params.append(product_id)
        self.conn.execute(query, tuple(params))
        self.conn.commit()

    def delete_product(self, product_id):
        query = "DELETE FROM products WHERE product_id = ?"
        self.conn.execute(query, (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        query = "SELECT * FROM products WHERE product_id = ?"
        cursor = self.conn.execute(query, (product_id,))
        return cursor.fetchone()

    def select_all_products(self):
        query = "SELECT * FROM products"
        cursor = self.conn.execute(query)
        return cursor.fetchall()

    def insert_sample_data(self, num_samples=100):
        product_names = [f"Product {i}" for i in range(1, num_samples + 1)]
        prices = [round(random.uniform(10.0, 1000.0), 2) for _ in range(num_samples)]

        for name, price in zip(product_names, prices):
            self.insert_product(name, price)

# Usage
store = ElectronicStore()
store.insert_sample_data()

# Test inserting a product
store.insert_product("New Product", 299.99)

# Test updating a product
store.update_product(1, product_name="Updated Product", price=399.99)

# Test selecting a product
print(store.select_product(1))

# Test deleting a product
store.delete_product(2)

# Test selecting all products
print(store.select_all_products())
