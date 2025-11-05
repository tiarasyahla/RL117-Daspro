# Tuple
a = ("apel", "jeruk", "ceri", "durian", "apel", 10, 20.3)

print(a)
print(len(a)) # Panjang tuple

print(a[3])
print(a[1:4])

# Mengganti item pada tuple dengan mengubahnya ke list terlebih dahulu
x = list(a)  # Mengubah tuple ke list
x[3] = "melon"  # Mengganti item pada list
a = tuple(x)  # Mengubah list kembali ke tuple
print(a)

# Menambah item pada tuple dengan mengubahnya ke list terlebih dahulu
x = list(a)
x.insert(1, "melon")
a = tuple(x)
print(a)

# Menghapus item pada tuple dengan mengubahnya ke list terlebih dahulu
x = list(a)
x.pop(2)
a = tuple(x)
print(a)

# Menambah item pada tuple dengan mengubahnya ke list terlebih dahulu
x = list(a)
x.append("mangga")
a = tuple(x)
print(a)

# Packing (bisa dilakukan juga di list)
buah = ("apel", "belimbing", "ceri", "durian")
(a, b, c, d) = buah
print(a)
print(b)
print(c)
print(d)
