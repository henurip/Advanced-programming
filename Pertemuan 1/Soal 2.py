totalBelanja = float(input("Masukkan total belanja Anda: Rp "))
ongkosKirim = 0

if 500 <= totalBelanja <= 300000:
    ongkosKirim = 0.1 * totalBelanja
elif 300000 < totalBelanja <= 500000:
    ongkosKirim = 0.05 * totalBelanja
else:
    ongkosKirim = 0

totalBayar = totalBelanja + ongkosKirim
print(f"Total belanja Anda: Rp {totalBelanja:.2f}")
print(f"Ongkos kirim: Rp {ongkosKirim:.2f}")
print(f"Total yang harus dibayar: Rp {totalBayar:.2f}")