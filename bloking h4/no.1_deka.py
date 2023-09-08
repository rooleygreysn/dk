import tkinter as tk

# Fungsi untuk menghitung total harga
def hitung_total():
    harga_barang = float(entry_harga.get())
    jumlah_barang = int(entry_jumlah.get())
    total_harga = harga_barang * jumlah_barang
    label_total.config(text=f"Total Harga: Rp {total_harga}")

# Membuat jendela utama
root = tk.Tk()
root.title("Program Kasir")

# Membuat label dan input untuk harga barang
label_harga = tk.Label(root, text="Harga Barang:")
label_harga.pack()
entry_harga = tk.Entry(root)
entry_harga.pack()

# Membuat label dan input untuk jumlah barang
label_jumlah = tk.Label(root, text="Jumlah Barang:")
label_jumlah.pack()
entry_jumlah = tk.Entry(root)
entry_jumlah.pack()

# Tombol untuk menghitung total harga
tombol_hitung = tk.Button(root, text="Hitung Total", command=hitung_total)
tombol_hitung.pack()

# Label untuk menampilkan total harga
label_total = tk.Label(root, text="")
label_total.pack()

# Menjalankan program
root.mainloop()