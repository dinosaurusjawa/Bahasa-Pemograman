import sqlite3

def insert_initial_data():
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()

    # Insert initial data into Products table
    cursor.executemany('''
    INSERT INTO Products (name, description, category, price, stock)
    VALUES (?, ?, ?, ?, ?)
    ''', [
        ('Jahe', 'Bahan Baku', 'Rempah Rempah', 10.99, 100),
        ('kemiri', 'Bahan Baku', 'Rempah Rempah', 15.99, 150)
    ])

    # Insert initial data into Users table
    cursor.executemany('''
    INSERT INTO Users (username, password, role)
    VALUES (?, ?, ?)
    ''', [
        ('admin', 'adminpass', 'admin'),
        ('user1', 'user1pass', 'user')
    ])

    # Insert initial data into Warehouses table
    cursor.executemany('''
    INSERT INTO Warehouses (name, location, capacity, current_stock)
    VALUES (?, ?, ?, ?)
    ''', [
        ('BantenJaya', 'Banten', 1000, 500),
        ('GoPIK', 'Jakarta', 2000, 1500)
    ])

    conn.commit()
    conn.close()
    print("Initial data inserted.")

if __name__ == '__main__':
    insert_initial_data()

