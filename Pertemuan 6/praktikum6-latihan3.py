#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
#======================================================

#======================================================
# Latihan 3 . Tracing Insertion Sort
# Data : [5, 2, 4, 6, 1, 3]
#======================================================

def insertion_sort_tracing(data):
    
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        jumlah_pergeseran = 0

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
            jumlah_pergeseran += 1

        data[j + 1] = key

        print("Iterasi i =", i, "->", data, "| Pergeseran =", jumlah_pergeseran)

    return data


# Data awal
data = [5, 2, 4, 6, 1, 3]
print("Data awal:", data)

# Menjalankan tracing
hasil = insertion_sort_tracing(data)

print("Hasil akhir:", hasil)


#======================================================
# Soal:
# 1. Tuliskan isi list setelah iterasi i = 1.
# 2. Tuliskan isi list setelah iterasi i = 3.
# 3. Berapa kali pergeseran terjadi pada iterasi i = 4?
#======================================================

# Jawaban:
# 1. Setelah iterasi i = 1:
#    [2, 5, 4, 6, 1, 3]

# 2. Setelah iterasi i = 3:
#    [2, 4, 5, 6, 1, 3]

# 3. Jumlah pergeseran pada iterasi i = 4 adalah 4 kali.