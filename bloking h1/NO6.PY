while True:
    nilai = int(input("masukkan nilai siswa : "))
    if nilai >= 75 :
        print("tuntas")
        break
    else:
        remed = input("mengulang [ya/tidak] : ")
        if remed == "tidak":
            print("tidak lulus")
            break