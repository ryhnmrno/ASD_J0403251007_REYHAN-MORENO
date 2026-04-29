#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 1 : Studi Kasus BFS (Jalur Terdekat Lokasi)
#======================================================

from collections import deque  # Mengimpor deque untuk antrian (queue) yang efisien

# Representasi graph menggunakan dictionary
# Key = node (lokasi), Value = list tetangga (node yang terhubung langsung)
graph = {
    'Rumah': ['Sekolah', 'Toko'],
    'Sekolah': ['Perpustakaan'],
    'Toko': ['Pasar'],
    'Perpustakaan': [],
    'Pasar': []
}

# Fungsi BFS (Breadth-First Search)
def bfs(graph, start):
    visited = set()           # Menyimpan node yang sudah dikunjungi agar tidak dikunjungi ulang
    queue = deque()           # Membuat queue (antrian) kosong

    visited.add(start)        # Menandai node awal sebagai sudah dikunjungi
    queue.append(start)       # Memasukkan node awal ke dalam queue

    # Selama queue masih ada isinya
    while queue:
        node = queue.popleft()    # Mengambil node paling depan dari queue
        print(node, end=" ")      # Menampilkan node (urutan kunjungan)

        # Mengunjungi semua tetangga dari node sekarang
        for neighbor in graph[node]:
            # Jika tetangga belum pernah dikunjungi
            if neighbor not in visited:
                visited.add(neighbor)   # Tandai sebagai sudah dikunjungi
                queue.append(neighbor)  # Masukkan ke queue untuk dikunjungi berikutnya

# Menjalankan BFS dari node 'Rumah'
print("BFS dari Rumah:")
bfs(graph, 'Rumah')


# =========================
# Jawaban Analisis
# =========================

# 1. Node mana yang dikunjungi pertama?
# Node pertama adalah 'Rumah', karena BFS selalu dimulai dari node start.

# 2. Mengapa BFS cocok untuk mencari jalur terdekat?
# BFS bekerja per level (melebar dulu, bukan dalam).
# Jadi node yang paling dekat (jumlah langkah paling sedikit) akan dikunjungi lebih dulu.
# Karena itu BFS cocok untuk mencari shortest path pada graph yang tidak berbobot.

# 3. Apa perbedaan urutan BFS jika struktur graph diubah?
# Urutan BFS tergantung:
# - Struktur hubungan node
# - Urutan isi list neighbor
#
# Jika urutan neighbor diubah, maka urutan kunjungan juga bisa berubah,
# walaupun tetap mengikuti konsep level-order (per tingkat).