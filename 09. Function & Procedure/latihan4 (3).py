# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

# Latihan 4

def validasi_harga(list_harga):
    valid = []
    for i in enumerate(list_harga):
        if harga <= 0:
            print(f"x Input tidak valid! Harga harus berupa angka positif.")
        else:
            valid.append(harga)
    return valid

def hitung_total(data):
    return sum(data)

def hitung_rata(data):
    return hitung_total / len(data)

def hasil(total, rata):
    print("\n=== HASIL ANALISIS PENJUALAN ===")
    print(f"Total Pendapatan: Rp {total:,.2f}")
    print(f"Rata-rata Pendapatan: Rp {rata:,.2f}")

def main():
    print("=== SISTEM ANALISIS PERFORMA PENJUALAN ===")

    n = int(input("Berapa banyak produk yang terjual hari ini? "))
    pendapatan = []

    for i in range(n):
        harga = float(input(f"Masukkan harga produk ke-{i+1}: Rp "))
        pendapatan.append(harga)
    
    pendapatan_valid = validasi_harga(pendapatan)
    total = hitung_total(pendapatan_valid)
    rata = hitung_rata(pendapatan_valid)

    hasil(total, rata)

main()
