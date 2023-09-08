# Definisikan kelas Contact
class Contact:
    def __init__(self, nama, nomor_telepon, email):
        self.nama = nama
        self.nomor_telepon = nomor_telepon
        self.email = email

    def tampilkan_info(self):
        print(f"Nama : {self.nama}")
        print(f"Nomor Telepon : {self.nomor_telepon}")
        print(f"Email : {self.email}")

# Definisikan kelas AddresBook untuk mengelola daftar kontak
class AddressBook:
    def __init__(self):
        self.daftar_kontak = []

    def tambah_kontak(self, kontak):
        self.daftar_kontak.append(kontak)

    def tampilkan_semua_kontak(self):
        print('daftar Kontak')
        for kontak in self.daftar_kontak:
            kontak.tampilkan_info()

# Program Utama
if __name__ == '__main__':
    addres_book = AddressBook()

    while True:
        print('Menu :')
        print('1. Tambah Kontak')
        print('2. Tampilkan semua Kontak')
        print('3. Keluar')

        pilihan = input('Pilih menu (1/2/3): ')

        if pilihan == '1':
            nama = input('Nama : ')
            nomor_telepon = input('Nomor Telepon : ')
            email = input('Email : ')
            kontak_baru = Contact(nama, nomor_telepon, email)
            addres_book.tambah_kontak(kontak_baru)
        elif pilihan == '2':
            addres_book.tampilkan_semua_kontak()
        elif pilihan == '3':
            break
        else:
            print('Pilihan tidak valid. Silakan pilih menu yang benar.')