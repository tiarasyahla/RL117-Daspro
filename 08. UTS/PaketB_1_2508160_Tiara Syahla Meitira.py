# Nama : Tiara Syahla Meitira
# NIM : 2508160
# Kelas : 1B
# UTS No. 1

print("Silakan Login!")
login_usn = input("Masukkan Username: ")
login_pw = input("Masukkan Password: ")

if login_usn!="GembiraMart!" or login_pw!="happy100%":
    print(f"Login Salah! Kesempatan tersisa 2 kali lagi")
    login_usn = input("Masukkan Username: ")
    login_pw = input("Masukkan Password: ")
    if login_usn!="GembiraMart!" or login_pw!="happy100%":
        print(f"Login Salah! Kesempatan tersisa 1 kali lagi")
        login_usn = input("Masukkan Username: ")
        login_pw = input("Masukkan Password: ")
        if login_usn!="GembiraMart!" or login_pw!="happy100%":
            print(f"Akses ditolak. Anda telah gagal login 3 kali. Silakan hubungi admin finance untuk mereset password")
        else:
            print("Login Berhasil! Selamat datang di sistem GembiraMart!")
    else:
        print("Login Berhasil! Selamat datang di sistem GembiraMart!")
else:
    print("Login Berhasil! Selamat datang di sistem GembiraMart!")
