# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B
# Paket Soal : Paket C

# Soal No. 5

barang = ["T-Shirt", "Blouse", "Kemeja", "Celana Panjang", "Rok", "Baju Renang", "Tas", "Topi", "Sepatu", "Sendal"]

print("------------------###------------------")

print("Daftar barang jualan Online Shop Nabila pada bulan juli: ")
for i in barang:
    print(i)
print("Jumlah barang: ", len(barang))

print("------------------###------------------")


# Daftar Barang Bulan Ini
barang[7] = "Dompet"

barang.append("Jepitan Rambut")
barang.append("Kerudung")

print("Daftar barang jualan Online Shop Nabila pada bulan ini: ")
for i in barang:
    print(i)
print("Jumlah barang: ", len(barang))

print("------------------###------------------")

