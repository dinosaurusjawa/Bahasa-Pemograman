import json
import os

class BahanBaku:
    def __init__(self, jenis, pemasok, waktu, lokasi, stok, tim_produksi):
        self.jenis = jenis
        self.pemasok = pemasok
        self.waktu = waktu
        self.lokasi = lokasi
        self.stok = stok
        self.tim_produksi = tim_produksi

    def to_dict(self):
        return {
            "jenis": self.jenis,
            "pemasok": self.pemasok,
            "waktu": self.waktu,
            "lokasi": self.lokasi,
            "stok": self.stok,
            "tim_produksi": self.tim_produksi
        }

    @staticmethod
    def from_dict(data):
        return BahanBaku(
            data['jenis'],
            data['pemasok'],
            data['waktu'],
            data['lokasi'],
            data['stok'],
            data['tim_produksi']
        )


class ManajemenBahanBaku:
    def __init__(self, filename='bahan_baku.json'):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump([bahan.to_dict() for bahan in self.data], file, indent=4)

    def add_bahan_baku(self, bahan):
        self.data.append(bahan)
        self.save_data()

    def update_bahan_baku(self, index, bahan):
        if 0 <= index < len(self.data):
            self.data[index] = bahan
            self.save_data()
        else:
            print("Indeks tidak valid.")

    def tampilkan_data(self):
        print("=== Daftar Bahan Baku ===")
        for i, bahan in enumerate(self.data):
            print(f"[{i}] {bahan['jenis']} | Pemasok: {bahan['pemasok']} | Stok: {bahan['stok']} | Tim Produksi: {bahan['tim_produksi']}")
        print("==========================\n")


def main():
    manajemen = ManajemenBahanBaku()

    while True:
        print("1. Tambah Bahan Baku")
        print("2. Update Bahan Baku")
        print("3. Tampilkan Data Bahan Baku")
        print("4. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == '1':
            jenis = input("Jenis Bahan Baku: ")
            pemasok = input("Pemasok: ")
            waktu = input("Waktu yang Diperlukan (hari): ")
            lokasi = input("Lokasi Pemberian Barang: ")
            stok = input("Stok Ketersediaan Setelah Dikirim (unit): ")
            tim_produksi = input("Tim Produksi: ")

            bahan_baku = BahanBaku(jenis, pemasok, waktu, lokasi, stok, tim_produksi)
            manajemen.add_bahan_baku(bahan_baku)

        elif pilihan == '2':
            manajemen.tampilkan_data()
            index = int(input("Pilih indeks bahan baku untuk diperbarui: "))
            jenis = input("Jenis Bahan Baku: ")
            pemasok = input("Pemasok: ")
            waktu = input("Waktu yang Diperlukan (hari): ")
            lokasi = input("Lokasi Pemberian Barang: ")
            stok = input("Stok Ketersediaan Setelah Dikirim (unit): ")
            tim_produksi = input("Tim Produksi: ")

            bahan_baku = BahanBaku(jenis, pemasok, waktu, lokasi, stok, tim_produksi)
            manajemen.update_bahan_baku(index, bahan_baku)

        elif pilihan == '3':
            manajemen.tampilkan_data()

        elif pilihan == '4':
            break

        else:
            print("Opsi tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
