#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 2 : Studi Kasus DFS (Eksplorasi Jalur)
#======================================================

# Representasi graph menggunakan dictionary
# Key = node, Value = list tetangga
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Fungsi DFS (Depth-First Search) menggunakan rekursi
def dfs(graph, node, visited):
    visited.add(node)        # Menandai node sebagai sudah dikunjungi
    print(node, end=" ")     # Menampilkan node saat dikunjungi

    # Loop semua tetangga dari node sekarang
    for neighbor in graph[node]:
        # Jika tetangga belum dikunjungi
        if neighbor not in visited:
            dfs(graph, neighbor, visited)  # Panggil DFS secara rekursif (masuk lebih dalam)

# Inisialisasi set untuk menyimpan node yang sudah dikunjungi
visited = set()

# Menjalankan DFS dari node 'A'
print("DFS dari A:")
dfs(graph, 'A', visited)


# =========================
# Jawaban Analisis
# =========================

# 1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
# Karena DFS menggunakan pendekatan rekursi (atau stack).
# Setiap kali menemukan node baru, DFS langsung masuk ke node tersebut
# sebelum mengecek node lain di level yang sama.
#
# Jadi alurnya seperti:
# A -> B -> D (habis) -> balik ke B -> E -> balik -> C -> F
#
# Ini yang membuat DFS terlihat seperti "menyelam" ke dalam dulu.

# 2. Apa yang terjadi jika urutan neighbor diubah?
# Urutan traversal DFS sangat bergantung pada urutan neighbor.
#
# Contoh:
# Jika 'A': ['C', 'B'], maka urutannya jadi:
# A -> C -> F -> B -> D -> E
#
# Jadi berbeda dengan BFS, DFS sangat sensitif terhadap urutan list.

# 3. Bandingkan hasil DFS dengan BFS pada graph yang sama
# BFS (level-order):
# A -> B -> C -> D -> E -> F
#
# DFS (depth-first):
# A -> B -> D -> E -> C -> F
#
# Perbedaannya:
# - BFS: menyebar dulu (cari yang dekat dulu)
# - DFS: masuk dalam dulu (jelajahi satu jalur sampai habis)
#
# Kesimpulan:
# BFS cocok untuk cari jalur terpendek,
# DFS cocok untuk eksplorasi semua kemungkinan jalur.