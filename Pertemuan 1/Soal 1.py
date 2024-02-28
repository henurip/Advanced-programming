jawab = 'ya'
total = 1
while(jawab.lower()=='ya'):
    angka = int(input('masukkan angka dalam range 0-50: '))
    if (0<=angka<=50):
        total = total + angka
    else:
        print('angka ',angka, 'diluar batas range')
    jawab = input('Apakah Anda masih ingin menambahkan angka lagi? ')
if (total%2 == 0):
    print('Jumlah keseluruhan angka yang Anda masukkan adalah ',total,' dan merupakan bilangan genap')
else:
    print('Jumlah keseluruhan angka yang Anda masukkan adalah ',total,' dan merupakan bilangan ganjil')