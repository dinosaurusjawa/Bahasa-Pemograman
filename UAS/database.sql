-- Membuat database
CREATE DATABASE PT_BahanBakuku;

-- Menggunakan database yang baru dibuat
USE PT_BahanBakuku;

-- Membuat tabel Pemasok
CREATE TABLE Pemasok (
    PemasokID INT PRIMARY KEY AUTO_INCREMENT,
    Nama VARCHAR(100) NOT NULL,
    Alamat VARCHAR(255),
    Telepon VARCHAR(20),
    Email VARCHAR(100),
    KontakPerson VARCHAR(100)
);

-- Membuat tabel BahanBaku
CREATE TABLE BahanBaku (
    BahanBakuID INT PRIMARY KEY AUTO_INCREMENT,
    Nama VARCHAR(100) NOT NULL,
    Kategori VARCHAR(100),
    Deskripsi TEXT,
    Unit VARCHAR(50)
);

-- Membuat tabel PesananPembelian
CREATE TABLE PesananPembelian (
    PesananID INT PRIMARY KEY AUTO_INCREMENT,
    PemasokID INT,
    TanggalPesanan DATE,
    TanggalPengiriman DATE,
    Status VARCHAR(50),
    TotalHarga DECIMAL(15, 2),
    FOREIGN KEY (PemasokID) REFERENCES Pemasok(PemasokID)
);

-- Membuat tabel DetailPesananPembelian
CREATE TABLE DetailPesananPembelian (
    DetailID INT PRIMARY KEY AUTO_INCREMENT,
    PesananID INT,
    BahanBakuID INT,
    Jumlah INT,
    HargaSatuan DECIMAL(15, 2),
    TotalHarga DECIMAL(15, 2),
    FOREIGN KEY (PesananID) REFERENCES PesananPembelian(PesananID),
    FOREIGN KEY (BahanBakuID) REFERENCES BahanBaku(BahanBakuID)
);

-- Membuat tabel Inventaris
CREATE TABLE Inventaris (
    InventarisID INT PRIMARY KEY AUTO_INCREMENT,
    BahanBakuID INT,
    Lokasi VARCHAR(100),
    Jumlah INT,
    TanggalUpdate DATE,
    FOREIGN KEY (BahanBakuID) REFERENCES BahanBaku(BahanBakuID)
);

-- Membuat tabel ProsesPengolahan
CREATE TABLE ProsesPengolahan (
    ProsesID INT PRIMARY KEY AUTO_INCREMENT,
    BahanBakuID INT,
    TanggalProses DATE,
    Jumlah INT,
    Status VARCHAR(50),
    Kualitas VARCHAR(50),
    FOREIGN KEY (BahanBakuID) REFERENCES BahanBaku(BahanBakuID)
);

-- Membuat tabel Distribusi
CREATE TABLE Distribusi (
    DistribusiID INT PRIMARY KEY AUTO_INCREMENT,
    BahanBakuID INT,
    Tujuan VARCHAR(255),
    TanggalPengiriman DATE,
    Jumlah INT,
    Status VARCHAR(50),
    FOREIGN KEY (BahanBakuID) REFERENCES BahanBaku(BahanBakuID)
);

-- Membuat tabel Pengguna
CREATE TABLE Pengguna (
    PenggunaID INT PRIMARY KEY AUTO_INCREMENT,
    Nama VARCHAR(100) NOT NULL,
    Posisi VARCHAR(100),
    Username VARCHAR(50) UNIQUE,
    Password VARCHAR(255),
    Email VARCHAR(100),
    NoTelepon VARCHAR(20)
);

-- Membuat tabel TransaksiPembayaran
CREATE TABLE TransaksiPembayaran (
    PembayaranID INT PRIMARY KEY AUTO_INCREMENT,
    PesananID INT,
    TanggalPembayaran DATE,
    JumlahPembayaran DECIMAL(15, 2),
    MetodePembayaran VARCHAR(50),
    Status VARCHAR(50),
    FOREIGN KEY (PesananID) REFERENCES PesananPembelian(PesananID)
);
