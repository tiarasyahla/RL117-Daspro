# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

jenis_kelamin = input("Masukkan Jenis Kelamin (Pria/Wanita) : ")
umur = int(input("Masukkan Umur : "))
tinggi_badan = int(input("Masukkan Tinggi Badan (dalam cm) : "))
iq = int(input("Masukkan IQ : "))

if (jenis_kelamin=="wanita" or jenis_kelamin=="Wanita"):
    if (umur>=18 and umur<=25):
        if (tinggi_badan==170):
            if (iq>=130):
                print("Selamat! Anda dapat menjadi seorang model catwalk.")
            else:
                print("Mohon maaf, IQ Anda tidak memenuhi batas minimal.")
        else:
            print("Mohon maaf, Tinggi Badan Anda tidak sesuai.")
    else:
        print("Mohon maaf, Umur Anda tidak memenuhi syarat.")
elif (jenis_kelamin=="pria" or jenis_kelamin=="Pria"):
    if (umur>=18 and umur<=25):
        if (tinggi_badan==175):
            if (iq>=130):
                print("Selamat! Anda dapat menjadi seorang model catwalk.")
            else:
                print("Mohon maaf, IQ Anda tidak memenuhi batas minimal.")
        else:
            print("Mohon maaf, Tinggi Badan Anda tidak sesuai.")
    else:
        print("Mohon maaf, Umur Anda tidak memenuhi syarat.")
else:
    print("Mohon masukkan jenis kelamin yang benar")
