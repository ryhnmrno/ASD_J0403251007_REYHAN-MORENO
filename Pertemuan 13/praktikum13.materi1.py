#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Materi 1 : Implementasi Kruskal
#======================================================

# Membuat daftar edge graph
# Format data:
# (bobot, node1, node2)

edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# List untuk menyimpan hasil MST
mst = []

# Variabel untuk menghitung total bobot
total_weight = 0

# Set untuk menyimpan node yang sudah terhubung
connected = set()

# Melakukan perulangan pada seluruh edge
for weight, u, v in edges:

    # Mengecek apakah edge membentuk cycle sederhana
    # Jika salah satu node belum terhubung,
    # maka edge dapat dipilih
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total bobot
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total_weight)


# ======================================================
# Penjelasan Program
# ======================================================
# Program ini merupakan implementasi sederhana
# algoritma Kruskal untuk mencari
# Minimum Spanning Tree (MST).
#
# MST adalah kumpulan edge yang dapat:
# - Menghubungkan semua node
# - Tidak membentuk cycle
# - Memiliki total bobot minimum
#
# Algoritma Kruskal bekerja dengan cara:
# 1. Mengurutkan edge dari bobot terkecil.
# 2. Memilih edge satu per satu.
# 3. Mengecek apakah edge membentuk cycle.
# 4. Jika tidak membentuk cycle maka edge dipilih.
#
# Pada graph ini edge yang dipilih adalah:
# - C ke D = 1
# - A ke C = 2
# - B ke D = 3
#
# Total bobot MST:
# 1 + 2 + 3 = 6
#
# Edge A-B dan A-D tidak dipilih karena
# semua node sudah terhubung dan jika ditambahkan
# dapat menyebabkan cycle.


# ======================================================
# Hasil Diskusi
# ======================================================
# Dari hasil diskusi dan percobaan program,
# algoritma Kruskal lebih fokus pada pemilihan
# edge dengan bobot terkecil secara global.
#
# Kelebihan algoritma ini:
# - Mudah dipahami
# - Cocok untuk sparse graph
# - Dapat menghasilkan total bobot minimum
#
# Kekurangannya:
# - Pada graph besar proses pengecekan cycle
#   bisa lebih rumit.
# - Biasanya membutuhkan struktur tambahan
#   seperti Union Find agar lebih efisien.
#
# Kesimpulan:
# Algoritma Kruskal sangat membantu dalam
# optimasi jaringan karena dapat mencari
# jalur dengan biaya minimum.