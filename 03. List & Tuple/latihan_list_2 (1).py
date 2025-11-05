# Nama: Tiara Syahla Meitira
# NIM: 2508160
# Kelas: 1B

# List
nilai = [88, 75, 63, 97, 82, 74, 91, 80, 81, 63]
print("Nilai 10 Mahasiswa:", nilai)

print("Nilai Maksimum: ", max(nilai)) # Nilai tertinggi
print("Nilai Minimum: ", min(nilai)) # Nilai terendah
print("Nilai Rata-Rata: ", avg := sum(nilai) / len(nilai)) # Rata-rata nilai

nilai.sort(reverse=True) # Mengurutkan nilai dari besar ke kecil
print("Urutan Nilai dari terbesar ke terkecil:", nilai)
print("Nilai terbesar kedua:", nilai[1]) # Nilai terbesar ke 2