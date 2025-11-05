# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

# Latihan 1

# 1. Deret Fibonacci menggunakan fungsi
print("1. Deret Fibonacci menggunakan fungsi")
def Fibonacci(n):
    a, b = 0, 1
    hasil = []
    for i in range(n):
        hasil.append(a)
        a, b = b, a + b
    return hasil

n = 10
print(f"Deret Fibonacci 10 angka: {Fibonacci(n)}")
print()


# 2. Menghitung volume tabung yang dibuat dalam sebuah fungsi
print("2. Menghitung volume tabung yang dibuat dalam sebuah fungsi")
def volume_tabung(r, t):
    pi = 22/7 
    return pi * r**2 * t

r = 14
t = 20
print("Jari-jari: ", r)
print("Tinggi: ", t)
print("Volume tabung: ", volume_tabung(r, t))


# 3. Menghitung fungsi nilai total dan nilai rata-rata berdasarkan nilai yag diinputkan dari nilai total
print("\n3. Menghitung fungsi nilai total dan nilai rata-rata berdasarkan nilai yag diinputkan dari nilai total")
def hitung_total_rata():
    angka = [2, 3, 5, 10]
    """while True:
        data = input("Masukkan angka (atau ketik 'stop' untuk selesai): ")
        if data.lower() == 'stop':
            break
        angka.append(float(data))
    
    if len(angka) == 0:
        print("Tidak ada data yang dimasukkan")
    else:"""
    total = sum(angka)
    rata = int(total / len(angka))

    print(f"Input: {angka}")
    print(f"Total: {angka[0]} + {angka[1]} + {angka[2]} + {angka[3]} = {total}")
    print(f"Rata-rata: {total} / {len(angka)} = {rata}")

hitung_total_rata()
