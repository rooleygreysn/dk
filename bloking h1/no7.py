nama = input("masukkan nama : ")
gaji = int(input("masukkan gaji pokok : "))

tunjangan = 20/100 * gaji
pajak = 15/100 * (gaji+tunjangan)
gajibersih = int(gaji + tunjangan - pajak)

print("--------------------------------")
print("nama :",nama)
print("gaji pokok:",gaji)
print("gaji bersih :",gajibersih)