#include <stdio.h>

void tambah();
void kurang();
void bagi();
void kali();

int main() {
    int pilihan;
    do {
        printf("\nKalkulator Sederhana\n");
        printf("1. Tambah\n");
        printf("2. Kurang\n");
        printf("3. Bagi\n");
        printf("4. Kali\n");
        printf("5. Keluar\n");
        printf("Pilih operasi (1-5): ");
        scanf("%d", &pilihan);

        switch (pilihan) {
            case 1:
                tambah();
                break;
            case 2:
                kurang();
                break;
            case 3:
                bagi();
                break;
            case 4:
                kali();
                break;
            case 5:
                printf("Keluar dari program.\n");
                break;
            default:
                printf("Pilihan tidak valid, coba lagi.\n");
                break;
        }
    } while (pilihan != 5);

    return 0;
}

void tambah() {
    int a, b;
    printf("Masukkan dua angka untuk ditambah: ");
    scanf("%d %d", &a, &b);
    printf("Hasil: %d\n", a + b);
}

void kurang() {
    int a, b;
    printf("Masukkan dua angka untuk dikurang: ");
    scanf("%d %d", &a, &b);
    printf("Hasil: %d\n", a - b);
}

void bagi() {
    float a, b;
    printf("Masukkan dua angka untuk dibagi: ");
    scanf("%f %f", &a, &b);
    if (b != 0) {
        printf("Hasil: %.2f\n", a / b);
    } else {
        printf("Kesalahan: Pembagian dengan nol tidak diperbolehkan.\n");
    }
}

void kali() {
    int a, b;
    printf("Masukkan dua angka untuk dikali: ");
    scanf("%d %d", &a, &b);
    printf("Hasil: %d\n", a * b);
}
