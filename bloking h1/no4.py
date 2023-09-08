a = int (input("masukkan jumlah baris : "))
bintang = "*"
for i in range(a):
    print(" " * (a - i - 1) + bintang)
    bintang += " *"