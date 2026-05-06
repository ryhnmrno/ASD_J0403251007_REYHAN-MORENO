#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 1 : Weighted Graph dan Perhitungan Jalur
#======================================================

# Membuat graph berbobot menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2},   # Node A ke B = 4, ke C = 2
    'B': {'D': 5},           # Node B ke D = 5
    'C': {'D': 1},           # Node C ke D = 1
    'D': {}                  # Node D tidak punya tetangga
}

# Menghitung total bobot jalur A -> B -> D
jalur_1 = graph['A']['B'] + graph['B']['D']  # 4 + 5

# Menghitung total bobot jalur A -> C -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # 2 + 1

# Menampilkan hasil jalur 1
print("Jalur 1: A -> B -> D =", jalur_1)

# Menampilkan hasil jalur 2
print("Jalur 2: A -> C -> D =", jalur_2)

# Membandingkan kedua jalur
if jalur_1 < jalur_2:  # jika jalur 1 lebih kecil
    print("Jalur terpendek adalah A -> B -> D")  # tampilkan jalur 1
else:  # jika tidak
    print("Jalur terpendek adalah A -> C -> D")  # tampilkan jalur 2

# =========================
# Jawaban Analisis:
# 1. Total bobot jalur A -> B -> D adalah 9, didapat dari penjumlahan 4 + 5.
#
# 2. Total bobot jalur A -> C -> D adalah 3, yaitu dari 2 + 1.
#
# 3. Jalur yang dipilih adalah A -> C -> D karena memiliki total bobot lebih kecil
#    dibandingkan jalur A -> B -> D.
#
# 4. Jalur terpendek tidak selalu berdasarkan jumlah edge paling sedikit,
#    karena dalam weighted graph yang diperhatikan adalah total bobot.
#    Bisa saja jalur lebih panjang (lebih banyak langkah) tetapi total bobotnya
#    lebih kecil, sehingga tetap menjadi jalur terbaik.
# =========================