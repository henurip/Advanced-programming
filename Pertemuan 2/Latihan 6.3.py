print("Sistem Deteksi Dini COVID 19")
print("-----------------------------")
nama = input("masukkan nama Anda")
print("Selamat datang",nama," jawablah pertanyaan berikut dengan ya atau tidak")

#Pertanyaan
dariLuarKota = input("Anda dari luar kota/luar negeri?")
demam = input("Anda mengalami demam?")
batuk = input("Anda mengalami batuk-batuk?")
sesak = input("Anda mengalami sesak napas?")

#Menghitung totalNilai, kondisi menggunakan operator ternary
totalNilai = 0
nilaiLuarKota=5 if (dariLuarKota.lower()=="ya") else 1
nilaiDemam=5 if (demam.lower()=="ya") else 1
nilaiBatuk=5 if (batuk.lower()=="ya") else 1
nilaiSesak=5 if (demam.lower()=="ya") else 1
totalNilai = nilaiLuarKota+nilaiDemam+nilaiBatuk+nilaiSesak

if(totalNilai>4):
    print(nama, "Anda perlu mengkarantina diri Anda selama 14 hari")
else:
    print(nama, "Anda sehat, gunakan masker selalu, terapkan social distancing")