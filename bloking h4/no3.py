from tkinter import *

# Membuat jendela utama
root = Tk()
root.title("Data Siswa Baru")

# Membuat fungsi untuk menampilkan data yang dimasukkan
def tampilkan_data():
    data = {
        "Nama Lengkap": nama.get(),
        "Tempat Lahir": tempat.get(),
        "Tanggal Lahir": tanggal.get(),
        "Sekolah": sekolah.get(),
        "Nama Ibu": ibu.get(),
        "Nama Ayah": ayah.get(),
        "No. Telepon": telepon.get(),
        "Alamat Rumah": alamat.get()
    }

    # Menghapus isi Listbox
    list_box.delete(0, END)

    # Menambahkan data ke Listbox
    for field, value in data.items():
        list_box.insert(END, f"{field}: {value}")

# Membuat variabel untuk menyimpan data
nama = StringVar()
tempat = StringVar()
tanggal = StringVar()
sekolah = StringVar()
ibu = StringVar()
ayah = StringVar()
telepon = StringVar()
alamat = StringVar()

# Membuat label dan entri untuk setiap bidang data
Label(root, text="Nama Lengkap:").grid(row=0, column=0, sticky=W)
Entry(root, textvariable=nama).grid(row=0, column=1, sticky=W)

Label(root, text="Tempat Lahir:").grid(row=1, column=0, sticky=W)
Entry(root, textvariable=tempat).grid(row=1, column=1, sticky=W)

Label(root, text="Tanggal Lahir:").grid(row=2, column=0, sticky=W)
Entry(root, textvariable=tanggal).grid(row=2, column=1, sticky=W)

Label(root, text="Sekolah:").grid(row=3, column=0, sticky=W)
Entry(root, textvariable=sekolah).grid(row=3, column=1, sticky=W)

Label(root, text="Nama Ibu:").grid(row=4, column=0, sticky=W)
Entry(root, textvariable=ibu).grid(row=4, column=1, sticky=W)

Label(root, text="Nama Ayah:").grid(row=5, column=0, sticky=W)
Entry(root, textvariable=ayah).grid(row=5, column=1, sticky=W)

Label(root, text="No. Telepon:").grid(row=6, column=0, sticky=W)
Entry(root, textvariable=telepon).grid(row=6, column=1, sticky=W)

Label(root, text="Alamat Rumah:").grid(row=7, column=0, sticky=W)
Entry(root, textvariable=alamat).grid(row=7, column=1, sticky=W)

# Membuat tombol untuk menampilkan data
Button(root, text="Tampilkan Data", command=tampilkan_data).grid(row=8, columnspan=2)

# Membuat Listbox untuk menampilkan hasil data
list_box = Listbox(root, width=40, height=10)
list_box.grid(row=9, columnspan=2)

# Menjalankan program
root.mainloop()