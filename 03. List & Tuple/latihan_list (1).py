# Nama: Tiara Syahla Meitira
# NIM: 2508160
# Kelas: 1B

# Latihan List
a = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]
print(a)

# Mengganti item pada list
a[2] = "cherry"
print(a)

# Menambah item oleh user
a.insert(int(input("Masukkan indeks: ")), input("Masukkan buah: "))
print(a)

# Mengurutkan list
a.sort()
print(a)