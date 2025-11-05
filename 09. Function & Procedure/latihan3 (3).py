# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

# Latihan 3

def hitung_selisih_detik(j1, m1, d1, j2, m2, d2):
    total_mulai = j1 * 3600 + m1 * 60 + d1
    total_selesai = j2 * 3600 + m2 * 60 + d2
    return total_selesai - total_mulai

def konversi(total_detik):
    jam = total_detik // 3600
    menit = (total_detik % 3600) // 60
    detik = total_detik % 60
    return jam, menit, detik

def hasil(j, m, d):
    print(f"Output: {j} jam {m} menit {d} detik")

def main():
    jam_mulai, menit_mulai, detik_mulai = 8, 10, 20
    jam_selesai, menit_selesai, detik_selesai = 9, 15, 30

    total_detik = hitung_selisih_detik(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)

    jam, menit, detik = konversi(total_detik)
    hasil(jam, menit, detik)

main()