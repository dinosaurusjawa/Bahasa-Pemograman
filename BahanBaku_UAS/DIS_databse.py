import sqlite3

def query_data():
    # Connect to SQLite database
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()

    # Query and display data
    print("Users:")
    cursor.execute("SELECT * FROM Users")
    for row in cursor.fetchall():
        print(row)

    print("\nWarehouses:")
    cursor.execute("SELECT * FROM Warehouses")
    for row in cursor.fetchall():
        print(row)

    print("\nProducts:")
    cursor.execute("SELECT * FROM Products")
    for row in cursor.fetchall():
        print(row)

    print("\nInventory:")
    cursor.execute("SELECT * FROM Inventory")
    for row in cursor.fetchall():
        print(row)

    print("\nShipments:")
    cursor.execute("SELECT * FROM Shipments")
    for row in cursor.fetchall():
        print(row)

    print("\nShipmentDetails:")
    cursor.execute("SELECT * FROM ShipmentDetails")
    for row in cursor.fetchall():
        print(row)

    print("\nSecurityLogs:")
    cursor.execute("SELECT * FROM SecurityLogs")
    for row in cursor.fetchall():
        print(row)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    query_data()
