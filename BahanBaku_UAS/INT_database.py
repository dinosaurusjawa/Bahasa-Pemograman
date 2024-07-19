import sqlite3

def setup_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()

    try:
        # Create tables
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Warehouses (
            warehouse_id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            manager_id INTEGER,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (manager_id) REFERENCES Users(user_id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            product_id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            description TEXT,
            category TEXT,
            unit_price REAL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Inventory (
            inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
            warehouse_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            location_in_warehouse TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id),
            FOREIGN KEY (product_id) REFERENCES Products(product_id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Shipments (
            shipment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            warehouse_id INTEGER NOT NULL,
            customer_id INTEGER NOT NULL,
            scheduled_date DATE NOT NULL,
            actual_ship_date DATE,
            status TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id),
            FOREIGN KEY (customer_id) REFERENCES Users(user_id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS ShipmentDetails (
            shipment_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
            shipment_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            quantity INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (shipment_id) REFERENCES Shipments(shipment_id),
            FOREIGN KEY (product_id) REFERENCES Products(product_id)
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS SecurityLogs (
            log_id INTEGER PRIMARY KEY AUTOINCREMENT,
            warehouse_id INTEGER,
            event_type TEXT NOT NULL,
            event_description TEXT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (warehouse_id) REFERENCES Warehouses(warehouse_id)
        )
        ''')

        # Commit changes
        conn.commit()
        print("Database and tables created successfully.")
    except sqlite3.OperationalError as e:
        print(f"OperationalError: {e}")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")
    except sqlite3.Error as e:
        print(f"SQLite Error: {e}")
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    setup_database()
