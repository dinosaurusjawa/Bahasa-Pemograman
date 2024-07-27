import sqlite3

# Membuat koneksi ke database SQLite (atau membuat database jika belum ada)
conn = sqlite3.connect('example.db')

# Membuat objek cursor untuk berinteraksi dengan database
cursor = conn.cursor()

# Menjalankan query untuk membuat tabel
cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    position TEXT
)
''')

# Menyisipkan data ke tabel
cursor.execute('''
INSERT INTO employees (name, position) VALUES (?, ?)
''', ('John Doe', 'Manager'))

# Menyimpan perubahan ke database
conn.commit()

# Menjalankan query untuk mengambil data
cursor.execute('SELECT * FROM employees')

# Mengambil semua baris hasil query
rows = cursor.fetchall()

for row in rows:
    print(row)

# Menutup cursor dan koneksi
cursor.close()
conn.close()
