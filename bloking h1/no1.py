user = input("menghituhng [persegi/panjang/trapesium] : ")

if user == "persegi" : 
    s = int(input("masukkan sisi : "))
    print("hasil keliling persegi adalah ",s*4)
    print("hasil luas persegi adalah ",s*s)

elif user == "persegi panjang" : 
    p = int(input("masukkan panjang : "))
    t = int(input("masukkan tinggi : "))
    print("hasil keliling persegi panjang adalah ", p+p+t+t)
    print("hasil luas persegi panjang adalah ", p*t)

elif user == "trapesium" : 
    a = int(input("masukkan atas : "))
    b = int(input("masukkan bawah : "))
    t = int(input("masukkan tinggi : "))
    m1 = int(input("masukkan sisi miring kanan : "))
    m2 = int(input("masukkan sisi miring kiri : "))
    print("hasil keliling trapesium adalah ", a+b+m1+m2)
    print("hasil luas trapesium adalah ", 1/2 * (a+b)*t)

else :
    print("masusukkan input yang benar !")
