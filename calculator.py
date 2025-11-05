print("Kalkulator sederhana 2 angka")
a = input("Masukkan angka pertama: ")
b = input("Masukkan angka kedua: ")

print("\n1. Penjumlahan \
2. Pengurangan \
3. Perkalian \
4. Pembagian")
angka = input("Pilih operasi matematika: ")

if angka == 1:
    print(a+b)
elif angka == 2:
    print(a-b)
elif angka == 3:
    print(a*b)
elif angka == 4:
    print(a/b)
else:
    print("pilihan tidak valid.")
