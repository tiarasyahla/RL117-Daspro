# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B
# Paket Soal : Paket C

# Soal No. 4

mobil = {
    "Merk" : "Honda",
    "Tipe" : "HRV",
    "Tahun" : 2018,
    "Warna" : "Hitam",
    "No. Polisi" : "D 1234 ABC",
    "Bensin" : "Pertalite",
    "Transmisi" : "Manual"
}

print("Mobil lama Pak Oki adalah: ")
print("Merk: ", mobil["Merk"])
print("Tipe: ", mobil["Tipe"])
print("Warna: ", mobil["Warna"])
print("Tahun: ", mobil["Tahun"])

print("------------------###------------------")

print("Merk: ", mobil["Merk"])
print("Tipe mobil: ", mobil["Tipe"])
print("Tahun keluaran: ", mobil["Tahun"])
print("Warna: ", mobil["Warna"])
print("No. Polisi: ", mobil["No. Polisi"])
print("Bensin: ", mobil["Bensin"])
print("Transmisi: ", mobil["Transmisi"])

k_baru = input(f"Masukan kategori (Contoh: Merk): ")
v_baru = input(f"Masukan informasi detail mobil baru (Contoh: HRV): ")

mobil[k_baru] = v_baru

print("Mobil baru Pak Oki adalah: ")
print("Merk: ", mobil["Merk"])
print("Tipe: ", mobil["Tipe"])
print("Warna: ", mobil["Warna"])
print("Tahun: ", mobil["Tahun"])
# mobil[{k_baru}] = v_baru

print("------------------###------------------")
