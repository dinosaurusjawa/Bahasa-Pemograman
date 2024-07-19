import sqlite3

def setup_database():
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()

    # Create Products table
    cursor.execute('''
    DROP TABLE IF EXISTS Products
    ''')
    cursor.execute('''
    CREATE TABLE Products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        category TEXT,
        price REAL NOT NULL,
        stock INTEGER NOT NULL DEFAULT 0
    )
    ''')

    # Create Users table
    cursor.execute('''
    DROP TABLE IF EXISTS Users
    ''')
    cursor.execute('''
    CREATE TABLE Users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )
    ''')

    # Create Warehouses table
    cursor.execute('''
    DROP TABLE IF EXISTS Warehouses
    ''')
    cursor.execute('''
    CREATE TABLE Warehouses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        location TEXT NOT NULL,
        capacity INTEGER NOT NULL,
        current_stock INTEGER NOT NULL DEFAULT 0
    )
    ''')

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == '__main__':
    setup_database()
