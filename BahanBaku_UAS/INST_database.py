import sqlite3

def insert_data():
    # Connect to SQLite database
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()

    try:
        # Insert sample data into Users
        users = [
            ("john_doe", "password123", "Admin"),
            ("jane_smith", "password456", "Warehouse Manager"),
            ("alice_johnson", "password789", "Customer"),
            ("bob_brown", "password000", "Logistics Manager"),
            ("carol_white", "password111", "Security Team")
        ]
        cursor.executemany("INSERT INTO Users (username, password, role) VALUES (?, ?, ?)", users)

        # Insert sample data into Warehouses
        warehouses = [
            ("Main Warehouse A", 2000, 1),
            ("Secondary Warehouse B", 1500, 2),
            ("Tertiary Warehouse C", 1000, 2)
        ]
        cursor.executemany("INSERT INTO Warehouses (location, capacity, manager_id) VALUES (?, ?, ?)", warehouses)

        # Insert sample data into Products
        products = [
            ("Steel Rods", "High-quality steel rods for construction", "Construction", 500.00),
            ("Copper Wires", "Copper wires used in electrical applications", "Electrical", 300.00),
            ("Aluminum Sheets", "Sheets of aluminum for manufacturing", "Manufacturing", 450.00),
            ("Plastic Granules", "Plastic granules for molding", "Plastic", 200.00)
        ]
        cursor.executemany("INSERT INTO Products (product_name, description, category, unit_price) VALUES (?, ?, ?, ?)", products)

        # Insert sample data into Inventory
        inventory = [
            (1, 1, 1000, "Rack 1"),
            (1, 2, 800, "Rack 2"),
            (2, 3, 600, "Rack 3"),
            (2, 4, 300, "Rack 4"),
            (3, 1, 400, "Rack 5"),
            (3, 2, 200, "Rack 6")
        ]
        cursor.executemany("INSERT INTO Inventory (warehouse_id, product_id, quantity, location_in_warehouse) VALUES (?, ?, ?, ?)", inventory)

        # Insert sample data into Shipments
        shipments = [
            (1, 3, '2024-07-25', None, 'Scheduled'),
            (2, 4, '2024-07-26', None, 'Scheduled'),
            (1, 2, '2024-07-27', None, 'Scheduled')
        ]
        cursor.executemany("INSERT INTO Shipments (warehouse_id, customer_id, scheduled_date, actual_ship_date, status) VALUES (?, ?, ?, ?, ?)", shipments)

        # Insert sample data into ShipmentDetails
        shipment_details = [
            (1, 1, 150),
            (1, 2, 100),
            (2, 4, 50),
            (3, 3, 200)
        ]
        cursor.executemany("INSERT INTO ShipmentDetails (shipment_id, product_id, quantity) VALUES (?, ?, ?)", shipment_details)

        # Insert sample data into SecurityLogs
        security_logs = [
            (1, 'Access', 'Access granted to user John Doe'),
            (1, 'Alarm', 'Fire alarm triggered in Main Warehouse A'),
            (2, 'Access', 'Access granted to user Jane Smith'),
            (3, 'Alarm', 'Security breach detected in Tertiary Warehouse C')
        ]
        cursor.executemany("INSERT INTO SecurityLogs (warehouse_id, event_type, event_description) VALUES (?, ?, ?)", security_logs)

        # Commit changes
        conn.commit()
        print("Sample data inserted successfully.")
    except sqlite3.IntegrityError as e:
        print(f"IntegrityError: {e}")
    except sqlite3.OperationalError as e:
        print(f"OperationalError: {e}")
    finally:
        # Close the connection
        conn.close()

if __name__ == "__main__":
    insert_data()
