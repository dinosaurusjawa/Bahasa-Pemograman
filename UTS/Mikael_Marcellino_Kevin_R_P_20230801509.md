# Soal 1
1. Jelaskan secara singkat apa itu paradigma dalam Bahasa Pemograman?
# Jawaban 
## JAWABAN ANDA 
Paradigma pemrograman merupakan gaya, klasifikasi, dan pendekatan dalam penulisan program untuk memecahkan masalah dengan menggunakan bahasa pemrograman yang digunakan.

# Soal 2
2. Jelaskan apa yang dimaksud dengan data lama,operator,seleksi dan fungsi?
# Jawaban
## JAWABAN ANDA
Model data adalah representasi abstrak dari struktur data yang digunakan dalam suatu sistem informasi atau program.

Operator adalah simbol yang digunakan untuk melakukan operasi pada nilai atau variabel.

Seleksi adalah cara yang digunakan program untuk mengambil keputusan ke satu kemungkinan dari beberapa kondisi.

Fungsi adalah suatu perintah dengan nama tertentu pada source code yang akan dipanggil untuk menjalankan tugas tertentu.


# Soal 3
3. Jelaskan komsep perulangan pernyataan (Looping Statement) di bawah ini :
```
int n, _, i, _;
cout << "Masukkan jumlah baris : ";
cin >> n;
for (i = l; i <= _; i++) (
    for (s = i;) _ <n; _++>
    cout << "";
    for (j = l; _ <= i; _++)
    cout << "*"
    cout << "\n";
)
```
Pecahkan perulangan di atas, berikan penjelasan terhadap program terebut dan keluaran dari program tersebut
# Jawaban
## JAWABAN ANDA (soal3.cpp)
```
for (i = 1; i <= n; i++) {}
```
Perulangan for ini berjalan dari 1 hingga n, mengontrol jumlah baris yang akan dicetak. i adalah variabel yang mewakili baris saat ini.
```
for (s = i; s < n; s++)
    cout << " ";
```
Perulangan for ini mencetak spasi untuk setiap baris. Jumlah spasi yang dicetak berkurang seiring bertambahnya baris. 
```
for (j = 1; j <= i; j++)
    cout << "*";
```
Perulangan for ini mencetak bintang untuk setiap baris.Misalnya, pada baris pertama (i=1) akan ada 1 bintang, pada baris kedua (i=2) akan ada 2 bintang, dan seterusnya.

Kesimpulannya perulangan code for pada program di atas akan selalu mencetak sesuai dengan inputan yang di inginkan user,tidak ada batas untuk perulangan for tersebut dan akan selalu menampilkan output rata kiri

# Soal 4
4. Buatlah program sederhana dengan hasil akhir seperti berikut :

"Berarti Usia Kalian sekarang adalah 21 Tahun"
# Jawaban
## JAWABAN ANDA (soal4.cpp)

# Soal 5
5. Buatlah program sederhana dengan hasil akhir seperti berikut :
```
Masukan Angka Pertama   : 10
Masukan Angka Kedua     : 2
Penjumlahan : 12
Pengurangan : 8
Perkalian   : 20
Pembagian   : 5
```
# Jawaban
## JAWABAN ANDA (soal5.cpp)

# Soal 6
6. Lengkapi penggalan source code berikut sehingga bisa berfungsi dengan baik :
```
int main(){
    menu();
    tambah();
    kurang();
    kali();
    bagi();
    return 0;
}
```
# Jawaban
## Jawaban ANDA (soal6.cpp)

# Soal 7 
7. Buatlah Diagram ALur/Flow yang sesuai dengan code yang anda lengkapi (Soal nomor 6) 
# Jawaban
## Jawaban Anda (soal6.puml)