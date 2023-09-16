jumlahPenumpang = int(input("Masukkan jumlah penumpang: "))
jumlahBus = jumlahPenumpang // 9
jumlahBusTambahan = jumlahPenumpang % 9

if jumlahBusTambahan > 0:
    jumlahBus += 1

jumlahOrangBerangkat = jumlahPenumpang + jumlahBus

print(f"Jumlah bus yang dibutuhkan: {jumlahBus} bus")
print(f"Jumlah orang yang berangkat: {jumlahOrangBerangkat} orang")