# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B

# Latihan 2

def cek_password(password):
    password_benar = "Latihan"
    return password == password_benar

def login(password):
    username = "Daspro2023"
    kesempatan = 3
    

    for i in range(kesempatan):
        print(f"Percobaan ke-{i+1}: password : {password}")

        if cek_password(password):
            print("Login berhasil! Selamat datang, Admin.")
            return
        else:
            print("Login gagal! Password salah.\n")

    print("Kesempatan habis! Akses ditolak.")

login("Latihan")
#login("latih")
#login("Latihan")