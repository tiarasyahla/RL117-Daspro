# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B
# UTS No. 4

jml = int(input("Masukkan jumlah produk: "))

for i in range(1, jml):
    print("-- Produk ke-", i)
    nama = input("Nama: ")
    total = int(input("Total Penjualan: "))

    print("\n-- Laporan Pendapatan Harian --")
    print(f"Total Pendapatan Seluruh Produk: Rp {sum(total)}")
    print(f"Rata-rata Pendapatan: Rp {sum(total)/len(total)}")
    print(f"Produk dengan Penjualan Tertinggi: ")
