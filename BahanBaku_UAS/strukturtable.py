import sqlite3

def insert_initial_data():
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()

    # Insert initial data into Products table
    cursor.executemany('''
    INSERT INTO Products (name, description, category, price, stock)
    VALUES (?, ?, ?, ?, ?)
    ''', [
        ('Jahe', 'BahanBaku', 'Category 1', 0.99, 100),
        ('Kemiri', 'BahanBaku', 'Category 1', 0.99, 150)
    ])

    # Insert initial data into Users table
    cursor.executemany('''
    INSERT INTO Users (username, password, role)
    VALUES (?, ?, ?)
    ''', [
        ('admin', 'adminpass', 'admin'),
        ('user1', 'user1pass', 'user')
    ])

    conn.commit()
    conn.close()
    print("Initial data inserted.")

if __name__ == '__main__':
    insert_initial_data()
