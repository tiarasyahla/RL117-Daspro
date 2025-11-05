# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

x = int(input("Masukkan bilangan : "))

if (x % 2 == 0):
    if (x >= 0):
        print("Bilangan", x, "adalah bilangan genap positif")
    else:
        print("Bilangan", x, "adalah bilangan genap negatif")
else:
    if (x >= 0):
        print("Bilangan", x, "adalah bilangan ganjil positif")
    else:
        print("Bilangan", x, "adalah bilangan ganjil negatif")
