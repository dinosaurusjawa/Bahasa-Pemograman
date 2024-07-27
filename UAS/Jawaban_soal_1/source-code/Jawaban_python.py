# Definisi fungsi rekursif untuk menghitung faktorial
def faktorial(n):
    # Kasus dasar: jika n adalah 0, kembalikan 1
    if n == 0:
        return 1
    # Kasus rekursif: n * faktorial dari (n - 1)
    else:
        return n * faktorial(n - 1)

# Memanggil fungsi rekursif dengan berbagai parameter
print(f"Faktorial dari 5 adalah {faktorial(5)}")
print(f"Faktorial dari 6 adalah {faktorial(6)}")
print(f"Faktorial dari 7 adalah {faktorial(7)}")
