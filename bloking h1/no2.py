user= input("menghitung[tabung/balok] : ")

if user == "tabung":
    t = int(input("masukkan tinggi : "))
    j = int(input("masukkan jari - jari : "))
    vol = 22/7*j*j*tprint("volume tabung : ", vol)

elif user == "balok":
    p = int(input("masukkan panjang : "))
    l = int(input("masukkan lebar : "))
    t = int(input("masukkan tinggi : "))
    print("volume balok : ",p*l*t)

else:
    print("tidak ada di daftar")