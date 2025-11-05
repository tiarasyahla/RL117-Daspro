# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B
# UTS No. 2

while True:
    input = int(input("Input penjualan: "))
    if input>=0:
        continue
    else:
        break

print(f"Total penjualan pada tanggal genap : {sum(input)}")
print(f"Total penjualan pada tanggal ganjil : {sum(input)}")
