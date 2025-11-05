# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

print("SISTEM BIAYA PARKIR DI MALL")

jam = int(input("\nMasukkan Durasi (jam & menit) \\" \
    "\n Jam :"))
menit = int(input("Menit : "))

durasi_menit = (jam*60) + menit
durasi_jam = durasi_menit/60

if durasi_jam <= 1.5:
    biaya = 5000
elif 1.5 < durasi_jam <= 4:
    biaya = 5000 + (durasi_jam/0.5*2000)
elif durasi_jam > 4:
    biaya = 5000 + 2000 * 5 + (durasi_jam/0.5*1000)
else:
    print()

print("Total biaya parkir yang harus dibayar : Rp", int(biaya))