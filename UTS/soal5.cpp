#include <iostream>

int main() {
    int angka1, angka2;

    std::cout << "Masukkan Angka Pertama   : ";
    std::cin >> angka1;
    std::cout << "Masukkan Angka Kedua     : ";
    std::cin >> angka2;

    int penjumlahan = angka1 + angka2;
    int pengurangan = angka1 - angka2;
    int perkalian = angka1 * angka2;
    float pembagian;
    if (angka2 != 0) {
        pembagian = static_cast<float>(angka1) / angka2;
    } else {
        std::cout << "Kesalahan: Pembagian dengan nol tidak diperbolehkan.\n";
        return 1;
    }

    std::cout << "Penjumlahan : " << penjumlahan << std::endl;
    std::cout << "Pengurangan : " << pengurangan << std::endl;
    std::cout << "Perkalian   : " << perkalian << std::endl;
    std::cout << "Pembagian   : " << pembagian << std::endl;

    return 0;
}
