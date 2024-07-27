import tkinter as tk
from tkinter import messagebox

# Fungsi yang dijalankan saat tombol diklik
def on_button_click():
    messagebox.showinfo("Informasi", "Tombol telah diklik!")

# Membuat jendela utama
window = tk.Tk()
window.title("Contoh GUI dengan Tkinter")
window.geometry("300x200")

# Membuat label
label = tk.Label(window, text="Hello, Selamat Datang di GUI Tkinter!", font=("Arial", 12))
label.pack(pady=20)

# Membuat tombol
button = tk.Button(window, text="Klik Saya", command=on_button_click, font=("Arial", 12))
button.pack(pady=10)

# Menjalankan loop utama aplikasi
window.mainloop()
