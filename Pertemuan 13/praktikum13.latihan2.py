#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 2 : Implementasi Sederhana Algoritma Kruskal
#======================================================

# Daftar edge graph
# Format:
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

# Menyimpan hasil MST
mst = []

# Menyimpan total bobot
total_weight = 0

# Set node yang sudah terhubung
connected = set()

# Membaca semua edge
for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total_weight)

# ======================================================
# Jawaban Analisis:
# 1. Edge pertama yang dipilih adalah C-D karena
#    memiliki bobot paling kecil yaitu 1.
#
# 2. Edge dengan bobot kecil dipilih lebih dahulu
#    agar total biaya MST menjadi minimum.
#
# 3. Total bobot MST yang dihasilkan adalah 6.
#
# 4. Edge tertentu tidak dipilih karena dapat
#    membentuk cycle atau memiliki bobot lebih besar.
# ======================================================