import mysql.connector
import inquirer
from mysql.connector import Error

# Konfigurasi koneksi
config = {
    'user': 'root',
    'password': 'password',  # Ganti dengan kata sandi Anda
    'host': 'localhost',
    'port': 3306,
    'host': 'localhost',
    'database': 'PT_BahanBakuku',
}

def create_connection():
    """Membuat koneksi ke database."""
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        if connection.is_connected():
            print("Berhasil terhubung ke database")
    except Error as e:
        print(f"Error: {e}")
    return connection

def fetch_tables(connection):
    """Mengambil daftar tabel dari database."""
    tables = []
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW TABLES;")
        tables = [table[0] for table in cursor.fetchall()]
    except Error as e:
        print(f"Error: {e}")
    return tables

def fetch_columns(connection, table_name):
    """Mengambil daftar kolom dari tabel tertentu."""
    columns = []
    try:
        cursor = connection.cursor()
        cursor.execute(f"DESCRIBE {table_name};")
        columns = [column[0] for column in cursor.fetchall()]
    except Error as e:
        print(f"Error: {e}")
    return columns

def fetch_data_from_table(connection, table_name):
    """Mengambil dan menampilkan data dari tabel tertentu."""
    try:
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        columns = fetch_columns(connection, table_name)
        print(f"Data dari tabel {table_name}:")
        print(columns)
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error: {e}")

def insert_data_into_table(connection, table_name):
    """Menambahkan data ke tabel tertentu."""
    columns = fetch_columns(connection, table_name)
    values = []
    for column in columns:
        value = input(f"Masukkan nilai untuk {column}: ")
        values.append(value)
    try:
        cursor = connection.cursor()
        placeholders = ', '.join(['%s'] * len(columns))
        cursor.execute(f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders});", values)
        connection.commit()
        print("Data berhasil ditambahkan.")
    except Error as e:
        print(f"Error: {e}")

def update_data_in_table(connection, table_name):
    """Mengubah data dalam tabel tertentu."""
    columns = fetch_columns(connection, table_name)
    id_column = columns[0]  # Asumsikan kolom pertama adalah ID atau primary key
    id_value = input(f"Masukkan {id_column} dari baris yang ingin diubah: ")
    updates = {}
    for column in columns[1:]:  # Tidak termasuk ID
        value = input(f"Masukkan nilai baru untuk {column} (biarkan kosong untuk tidak mengubah): ")
        if value:
            updates[column] = value
    if updates:
        set_clause = ', '.join([f"{col} = %s" for col in updates.keys()])
        values = list(updates.values())
        values.append(id_value)
        try:
            cursor = connection.cursor()
            cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE {id_column} = %s;", values)
            connection.commit()
            print("Data berhasil diubah.")
        except Error as e:
            print(f"Error: {e}")

def delete_data_from_table(connection, table_name):
    """Menghapus data dari tabel tertentu."""
    columns = fetch_columns(connection, table_name)
    id_column = columns[0]  # Asumsikan kolom pertama adalah ID atau primary key
    id_value = input(f"Masukkan {id_column} dari baris yang ingin dihapus: ")
    try:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM {table_name} WHERE {id_column} = %s;", (id_value,))
        connection.commit()
        print("Data berhasil dihapus.")
    except Error as e:
        print(f"Error: {e}")

def main():
    connection = create_connection()
    if connection:
        while True:
            action_question = [
                inquirer.List('action',
                              message="Pilih aksi yang ingin dilakukan",
                              choices=['Lihat Data', 'Tambah Data', 'Ubah Data', 'Hapus Data', 'Keluar'],
                              ),
            ]
            action_answer = inquirer.prompt(action_question)
            action = action_answer['action']
            if action == 'Keluar':
                break

            tables = fetch_tables(connection)
            if not tables:
                print("Tidak ada tabel yang ditemukan dalam database.")
                continue

            table_question = [
                inquirer.List('table',
                              message="Pilih tabel yang ingin dikelola",
                              choices=tables,
                              ),
            ]
            table_answer = inquirer.prompt(table_question)
            selected_table = table_answer['table']
            
            if action == 'Lihat Data':
                fetch_data_from_table(connection, selected_table)
            elif action == 'Tambah Data':
                insert_data_into_table(connection, selected_table)
            elif action == 'Ubah Data':
                update_data_in_table(connection, selected_table)
            elif action == 'Hapus Data':
                delete_data_from_table(connection, selected_table)

        if connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()
