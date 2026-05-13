#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 5 : Tugas Mandiri: Buat Program MST dengan Kasus Baru
#======================================================

# Membuat daftar edge graph
# Format:
# (bobot, node1, node2)

edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# List untuk menyimpan hasil MST
mst = []

# Variabel untuk menghitung total bobot MST
total_weight = 0

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Perulangan untuk membaca seluruh edge
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan setiap edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot minimum
print("Total bobot minimum =", total_weight)


# ======================================================
# Penjelasan Program
# ======================================================
# Program ini digunakan untuk mencari
# Minimum Spanning Tree (MST)
# pada kasus jaringan jalan antar kota.
#
# Algoritma yang digunakan adalah Kruskal.
#
# Cara kerja algoritma Kruskal:
# 1. Mengurutkan semua edge dari bobot terkecil.
# 2. Memilih edge dengan bobot paling kecil.
# 3. Mengecek apakah edge membentuk cycle.
# 4. Jika tidak membentuk cycle maka edge dipilih.
# 5. Proses diulang sampai semua node terhubung.
#
# Pada program ini digunakan list dan set sederhana.
#
# Hasil MST:
# Bogor - Depok = 2
# Depok - Jakarta = 3
# Depok - Bandung = 4
#
# Total bobot MST:
# 2 + 3 + 4 = 9


# ======================================================
# Jawaban Analisis
# ======================================================
# 1. Kasus apa yang dipilih?
# Jawab:
# Kasus yang dipilih adalah jaringan jalan antar kota.
#
# 2. Algoritma apa yang digunakan?
# Jawab:
# Algoritma yang digunakan adalah Kruskal.
#
# 3. Edge mana saja yang dipilih dalam MST?
# Jawab:
# Edge yang dipilih yaitu:
# - Bogor ke Depok = 2
# - Depok ke Jakarta = 3
# - Depok ke Bandung = 4
#
# 4. Berapa total bobot MST?
# Jawab:
# Total bobot MST adalah 9.
#
# 5. Mengapa edge tertentu tidak dipilih?
# Jawab:
# Karena edge tersebut memiliki bobot lebih besar
# atau dapat membentuk cycle sehingga tidak efisien
# untuk digunakan dalam MST.