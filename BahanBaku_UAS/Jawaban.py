import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

def add_data(table, data):
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()
    try:
        if table == 'Products':
            query = '''
            INSERT INTO Products (name, description, category, price, stock)
            VALUES (?, ?, ?, ?, ?)
            '''
        elif table == 'Users':
            query = '''
            INSERT INTO Users (username, password, role)
            VALUES (?, ?, ?)
            '''
        else:
            raise ValueError(f"Unsupported table: {table}")

        cursor.execute(query, data)
        conn.commit()
        messagebox.showinfo("Success", "Data added successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"SQLite Error: {e}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

def handle_add():
    table = simpledialog.askstring("Input", "Enter table name (Products or Users):")
    if table == 'Products':
        name = simpledialog.askstring("Input", "Enter product name:")
        description = simpledialog.askstring("Input", "Enter product description:")
        category = simpledialog.askstring("Input", "Enter product category:")
        price = simpledialog.askfloat("Input", "Enter product price:")
        stock = simpledialog.askinteger("Input", "Enter product stock:")
        data = (name, description, category, price, stock)
        add_data(table, data)
    elif table == 'Users':
        username = simpledialog.askstring("Input", "Enter username:")
        password = simpledialog.askstring("Input", "Enter password:")
        role = simpledialog.askstring("Input", "Enter role (admin or user):")
        data = (username, password, role)
        add_data(table, data)
    else:
        messagebox.showwarning("Warning", "Unsupported table name.")

def update_data(table, column, value, condition_column, condition_value):
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()
    try:
        query = f"UPDATE {table} SET {column} = ? WHERE {condition_column} = ?"
        cursor.execute(query, (value, condition_value))
        conn.commit()
        if cursor.rowcount == 0:
            messagebox.showwarning("Warning", "No rows updated. Check the condition value.")
        else:
            messagebox.showinfo("Success", "Data updated successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"SQLite Error: {e}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

def delete_data(table, condition_column, condition_value):
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()
    try:
        query = f"DELETE FROM {table} WHERE {condition_column} = ?"
        cursor.execute(query, (condition_value,))
        conn.commit()
        if cursor.rowcount == 0:
            messagebox.showwarning("Warning", "No rows deleted. Check the condition value.")
        else:
            messagebox.showinfo("Success", "Data deleted successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"SQLite Error: {e}")
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    finally:
        conn.close()

def handle_update():
    table = simpledialog.askstring("Input", "Enter table name (Products or Users):")
    column = simpledialog.askstring("Input", "Enter column name to update:")
    value = simpledialog.askstring("Input", "Enter new value:")
    condition_column = simpledialog.askstring("Input", "Enter column name for condition:")
    condition_value = simpledialog.askstring("Input", "Enter condition value:")
    update_data(table, column, value, condition_column, condition_value)

def handle_delete():
    table = simpledialog.askstring("Input", "Enter table name (Products or Users):")
    condition_column = simpledialog.askstring("Input", "Enter column name for condition:")
    condition_value = simpledialog.askstring("Input", "Enter condition value:")
    delete_data(table, condition_column, condition_value)

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")

# Create and place buttons
add_button = tk.Button(root, text="Add Data", command=handle_add)
add_button.pack(pady=10)

update_button = tk.Button(root, text="Update Data", command=handle_update)
update_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Data", command=handle_delete)
delete_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
