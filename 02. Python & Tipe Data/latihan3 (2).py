a = """Ini adalah contoh
dari multi line
string"""
print(a)

b = "Halo, apa kabar?"
print(b[1:4]) # mulai dari index 1 sampai 4 (tidak termasuk index 4)
print(b[:5]) # mulai dari index 0 sampai 5 (tidak termasuk index 5)
print(b[10:]) # mulai dari index 10 sampai akhir
print(b[-5:-1]) # mulai dari index -5 sampai -1 (tidak termasuk index -1)
print(b[-5:]) # mulai dari index -5 sampai akhir
print(b[:-1]) # mulai dari index 0 sampai -1 (tidak termasuk index -1)
print(b[-1]) # index -1
print(b[::2]) # mulai dari index 0 sampai akhir, dengan step 2
print(b[1::2]) # mulai dari index 1 sampai akhir, dengan step 2
print(b[::-1]) # membalik string

print(len(b)) # panjang string
print(type(b)) # tipe data string

print(b.lower()) # mengubah string menjadi huruf kecil
print(b.upper()) # mengubah string menjadi huruf besar

print(b.strip())

print(b.replace("Halo", "Hi")) # mengganti kata Halo dengan Hi
print(b.split(",")) # memisahkan string berdasarkan koma

text = "Halo, Selamat datang \"Tiara\" dari Bandung."
print(text)