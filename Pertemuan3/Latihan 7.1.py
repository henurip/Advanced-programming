print("Sistem Deteksi Dini COVID 19")
print("-----------------------------")
print()
#deklarasi list outer
data = []
for i in range(3):
    #deklarasi list inner
    baris = []
    #pertanyaan
    nama = input("masukkan nama Anda")
    print("Selamat datang",nama," jawablah pertanyaan berikut dengan ya atau tidak")
    dariLuarKota = input("Anda dari luar kota/luar negeri?")
    demam = input("Anda mengalami demam?")
    batuk = input("Anda mengalami batuk-batuk?")
    sesak = input("Anda mengalami sesak napas?")
    print()
    #input ke list inner
    baris.append(nama)
    baris.append(dariLuarKota)
    baris.append(demam)
    baris.append(batuk)
    baris.append(sesak)
    #input ke list outer
    data.append(baris)
#Cetak 
print("Data")
for baris in data:
    i=0
    print("Nama:",baris[i])
    print("Dari luar kota:",baris[i+1])
    print("Demam:",baris[i+2])
    print("Batuk:",baris[i+3])
    print("Sesak napas:",baris[i+4])
    print()

    
    
