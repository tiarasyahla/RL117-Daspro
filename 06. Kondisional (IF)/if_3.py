# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

x = int(input("Masukkan nilai : "))

if (100 >= x and x >= 90):
    print("Nilai Anda adalah A")
elif (90 > x and x >= 80):
    print("Nilai Anda adalah B")
elif (80 > x and x >= 70):
    print("Nilai Anda adalah C")
elif (x < 70):
    print("Nilai Anda adalah D")
else:
    print("Nilai tidak valid")
