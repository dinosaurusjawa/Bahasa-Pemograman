import mysql.connector
from mysql.connector import Error

# Konfigurasi koneksi ke database
config = {
    'user': 'root',  # Ganti dengan nama pengguna Anda
    'password': 'password',  # Ganti dengan kata sandi Anda
    'host': 'localhost',
    'port': 3306,
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

def create_tables(connection):
    """Membuat tabel-tabel di database."""
    cursor = connection.cursor()
    tables = [
        """
        CREATE TABLE IF NOT EXISTS Pemasok (
            PemasokID INT PRIMARY KEY AUTO_INCREMENT,
            Nama VARCHAR(100) NOT NULL,
            Alamat VARCHAR(255),
            Telepon VARCHAR(20),
            Email VARCHAR(100),
            KontakPerson VARCHAR(100)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS BahanBaku (
            BahanBakuID INT PRIMARY KEY AUTO_INCREMENT,
            Nama VARCHAR(100) NOT NULL,
            Kategori VARCHAR(100),
            Deskripsi TEXT,
            Unit VARCHAR(50)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS PesananPembelian (
            PesananID INT PRIMARY KEY AUTO_INCREMENT,
            PemasokID INT,
            TanggalPesanan DATE,
            TanggalPengiriman DATE,
            Status VARCHAR(50),
            TotalHarga DECIMAL(15, 2),
            FOREIGN KEY (PemasokID) REFERENCES Pemasok(PemasokID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS DetailPesananPembelian (
            DetailID INT PRIMARY KEY AUTO_INCREMENT,
            PesananID INT,
            BahanBakuID INT,
            Jumlah INT,
            HargaSatuan DECIMAL(15, 2),
            TotalHarga DECIMAL(15, 2),
            FOREIGN KEY (PesananID) REFERENCES PesananPembelian(PesananID),
            FOREIGN KEY (BahanBakuID) REFERENCES BahanBaku(BahanBakuID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Inventaris (
            InventarisID INT PRIMARY KEY AUTO_INCREMENT,
            BahanBakuID INT,
            Lokasi VARCHAR(100),
            Jumlah INT,
            TanggalUpdate DATE,
            FOREIGN KEY (BahanBakuID) REFERENCES BahanBaku(BahanBakuID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS ProsesPengolahan (
            ProsesID INT PRIMARY KEY AUTO_INCREMENT,
            BahanBakuID INT,
            TanggalProses DATE,
            Jumlah INT,
            Status VARCHAR(50),
            Kualitas VARCHAR(50),
            FOREIGN KEY (BahanBakuID) REFERENCES BahanBaku(BahanBakuID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Distribusi (
            DistribusiID INT PRIMARY KEY AUTO_INCREMENT,
            BahanBakuID INT,
            Tujuan VARCHAR(255),
            TanggalPengiriman DATE,
            Jumlah INT,
            Status VARCHAR(50),
            FOREIGN KEY (BahanBakuID) REFERENCES BahanBaku(BahanBakuID)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS Pengguna (
            PenggunaID INT PRIMARY KEY AUTO_INCREMENT,
            Nama VARCHAR(100) NOT NULL,
            Posisi VARCHAR(100),
            Username VARCHAR(50) UNIQUE,
            Password VARCHAR(255),
            Email VARCHAR(100),
            NoTelepon VARCHAR(20)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS TransaksiPembayaran (
            PembayaranID INT PRIMARY KEY AUTO_INCREMENT,
            PesananID INT,
            TanggalPembayaran DATE,
            JumlahPembayaran DECIMAL(15, 2),
            MetodePembayaran VARCHAR(50),
            Status VARCHAR(50),
            FOREIGN KEY (PesananID) REFERENCES PesananPembelian(PesananID)
        );
        """
    ]
    
    for table in tables:
        try:
            cursor.execute(table)
            print("Tabel berhasil dibuat atau sudah ada")
        except Error as e:
            print(f"Error: {e}")
    
    cursor.close()

def insert_pemasok(connection, nama, alamat, telepon, email, kontak_person):
    """Menambahkan data ke tabel Pemasok."""
    query = """
    INSERT INTO Pemasok (Nama, Alamat, Telepon, Email, KontakPerson)
    VALUES (%s, %s, %s, %s, %s);
    """
    values = (nama, alamat, telepon, email, kontak_person)
    cursor = connection.cursor()
    try:
        cursor.execute(query, values)
        connection.commit()
        print("Data berhasil ditambahkan ke tabel Pemasok")
    except Error as e:
        print(f"Error: {e}")
    cursor.close()

def fetch_pemasok(connection):
    """Mengambil data dari tabel Pemasok."""
    query = "SELECT * FROM Pemasok;"
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Error as e:
        print(f"Error: {e}")
    cursor.close()

def main():
    """Fungsi utama untuk menjalankan script."""
    connection = create_connection()
    if connection:
        create_tables(connection)
        insert_pemasok(connection, 'PT Contoh Pemasok', 'Jl. Contoh No.1', '1234567890', 'contoh@pemasok.com', 'John Doe')
        fetch_pemasok(connection)
        connection.close()

if __name__ == "__main__":
    main()
