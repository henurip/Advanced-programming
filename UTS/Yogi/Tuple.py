buah_buahan_1  = ("Apel, Jeruk, Mangga, Semangka")

print(buah_buahan_1)

buah_buahan_2 =("Pisang, Anggur, Pepaya, Manggis")

print(buah_buahan_2)

#menggabungkan dua tuple  menjadi satu
semua_buah_buahan = buah_buahan_1 + buah_buahan_2

print(semua_buah_buahan)

#mengimplemntasikan fungsi hitung jumlah elemen-elemen tuple
def mysum(*a):
    total = 0
    for ele in a:
        print(total,"+",ele,"=",end=' ')
        total += ele #total=total+ele
        print(total)
    return total

print(mysum(94,2,7,8))

