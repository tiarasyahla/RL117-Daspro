print("Kalkulator sederhana 2 angka")
a = input("Masukkan angka pertama: ")
b = input("Masukkan angka kedua: ")

print("\n1. Penjumlahan \
2. Pengurangan (a+b) \
3. Perkalian (a*b) \
4. Pembagian (a/b) \
5. Pangkat (a^b)")
angka = input("Pilih operasi matematika: ")

if angka == 1:
    print(a+b)
elif angka == 2:
    print(a-b)
elif angka == 3:
    print(a*b)
elif angka == 4:
    print(a/b)
elif angka == 5:
    print(a**b)
else:
    print("pilihan tidak valid.")
