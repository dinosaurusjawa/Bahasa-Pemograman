def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
        return None
    except TypeError:
        print("Kesalahan: Kedua argumen harus berupa angka.")
        return None
    else:
        print(f"Hasil pembagian: {result}")
        return result
    finally:
        print("Blok finally dieksekusi.")

# Contoh pemanggilan fungsi dengan berbagai skenario
print("Contoh 1: Pembagian normal")
divide_numbers(10, 2)

print("\nContoh 2: Pembagian dengan nol")
divide_numbers(10, 0)

print("\nContoh 3: Argumen bukan angka")
divide_numbers(10, "a")
