#Buatlah sebuah tuple yang berisi bberapa nama buah-buahan

buah1 = ('apel', 'anggur', 'jeruk')

print(buah1)

#Implementasikan program untuk menggabungkan dua tuple menjadi satu
buah2 = ('semangka', 'nanas', 'pepaya')

print(buah2)

buah12 = buah1+buah2

print(buah12)

#Buatlah sebuah tuple yang berisi nilai-nilai numerik dan implementasikan fungsi untuk menghitung jumla elemen-elemen tuple tersebut
def angka(*a):
    jumlah = 0
    for anggota in a:
        print(jumlah,"+",anggota,"=",end=' ')
        jumlah += ele
        print(jumlah)
    return jumlah

print(angka(1,2,3,4,5))