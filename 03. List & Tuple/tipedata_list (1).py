# List
a = ["apel", "jeruk", "ceri", "durian", "apel"]

print(len(a)) # Panjang list

print(a[2])
print(a[1:4])

# Menambah item ke list
a.append("sirsak")
print(a)

a[2] = "manggis"
print(a)

a.insert(3, "semangka")
print(a)

a.insert(10, "kiwi")
print(a)

# Menghapus item dari list
a.pop(3)
print(a)

# Menambah list dengan list lain
b = ["strawberry", "blueberry"]
print(a)
a.extend(b)
print(a)

# Mengurutkan list
print(a)
a.sort()
print(a)
a.sort(reverse=True)
print(a)

