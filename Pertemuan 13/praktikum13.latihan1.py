#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 1 : Memahami Konsep Spanning Tree
#======================================================

# Membuat daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Membuat contoh spanning tree
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan semua edge graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge graph
print("\nJumlah edge graph =", len(edges))

# Menampilkan jumlah edge spanning tree
print("Jumlah edge spanning tree =", len(spanning_tree))

# ======================================================
# Jawaban Analisis:
# 1. Graph awal memiliki lebih banyak hubungan antar
#    node dan dapat memiliki cycle.
#    Spanning tree hanya mengambil edge penting saja.
#
# 2. Cycle tidak boleh ada karena membuat graph menjadi
#    tidak efisien dan menambah biaya.
#
# 3. Jumlah edge spanning tree lebih sedikit karena
#    hanya memakai edge minimum untuk menghubungkan
#    semua node.
# ======================================================