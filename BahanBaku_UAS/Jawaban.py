import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog

# Function to update data in the database
def update_data(table, column, value, condition_column, condition_value):
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()
    try:
        query = f"UPDATE {table} SET {column} = ? WHERE {condition_column} = ?"
        cursor.execute(query, (value, condition_value))
        conn.commit()
        messagebox.showinfo("Success", "Data updated successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"SQLite Error: {e}")
    finally:
        conn.close()

# Function to delete data from the database
def delete_data(table, condition_column, condition_value):
    conn = sqlite3.connect('inventory_management.db')
    cursor = conn.cursor()
    try:
        query = f"DELETE FROM {table} WHERE {condition_column} = ?"
        cursor.execute(query, (condition_value,))
        conn.commit()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"SQLite Error: {e}")
    finally:
        conn.close()

# Function to handle update operation
def handle_update():
    table = simpledialog.askstring("Input", "Enter table name (e.g., Products):")
    column = simpledialog.askstring("Input", "Enter column name to update:")
    value = simpledialog.askstring("Input", "Enter new value:")
    condition_column = simpledialog.askstring("Input", "Enter column name for condition:")
    condition_value = simpledialog.askstring("Input", "Enter condition value:")
    if table and column and value and condition_column and condition_value:
        update_data(table, column, value, condition_column, condition_value)

# Function to handle delete operation
def handle_delete():
    table = simpledialog.askstring("Input", "Enter table name (e.g., Products):")
    condition_column = simpledialog.askstring("Input", "Enter column name for condition:")
    condition_value = simpledialog.askstring("Input", "Enter condition value:")
    if table and condition_column and condition_value:
        delete_data(table, condition_column, condition_value)

# Create the main window
root = tk.Tk()
root.title("Inventory Management System")

# Create and place buttons
update_button = tk.Button(root, text="Update Data", command=handle_update)
update_button.pack(pady=10)

delete_button = tk.Button(root, text="Delete Data", command=handle_delete)
delete_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
