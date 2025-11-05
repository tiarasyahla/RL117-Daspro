# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

print("### PROGRAM KALKULATOR BMI ###")
bb = int(input("Masukkan Berat Badan (kg) : "))
tb = int(input("Masukkan Tinggi Badan (cm) : "))

tb_meter = round(tb/100)

bmi = bb / (tb_meter*tb_meter)

if bmi < 18.5:
    print("BMI : ", int(bmi))
    print("Kategori: Kurus")
elif 18.5 <= bmi < 25:
    print("BMI : ", int(bmi))
    print("Kategori: Normal")
elif 25 <= bmi < 30:
    print("BMI : ", int(bmi))
    print("Kategori: Berlebih")
elif bmi >= 30:
    print("BMI : ", int(bmi))
    print("Kategori: Obesitas")
else:
    print("Sepertinya ada yang salah?")
