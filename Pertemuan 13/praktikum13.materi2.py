#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Materi 2 : Algoritma Prim
#======================================================

# Mengimpor library heapq
# heapq digunakan untuk mengambil edge
# dengan bobot terkecil secara otomatis
import heapq

# Membuat weighted graph menggunakan dictionary
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Membuat fungsi prim()
# Fungsi ini digunakan untuk mencari MST
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # List untuk menyimpan edge kandidat
    edges = []

    # List untuk menyimpan hasil MST
    mst = []

    # Variabel untuk menghitung total bobot
    total_weight = 0

    # Mengambil semua tetangga dari node awal
    for neighbor, weight in graph[start].items():

        # Menambahkan edge ke priority queue
        heapq.heappush(edges, (weight, start, neighbor))

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total
            total_weight += weight

            # Mengecek tetangga node baru
            for neighbor, w in graph[v].items():

                # Jika tetangga belum dikunjungi
                if neighbor not in visited:

                    # Menambahkan edge baru ke heap
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight


# Memanggil fungsi prim()
# Node awal dimulai dari A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan setiap edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot MST
print("Total bobot =", total)


# ======================================================
# Penjelasan Program
# ======================================================
# Program ini merupakan implementasi algoritma Prim
# untuk mencari Minimum Spanning Tree (MST).
#
# Algoritma Prim bekerja dengan cara:
# 1. Memulai dari satu node awal.
# 2. Memilih edge dengan bobot terkecil.
# 3. Menambahkan node baru ke dalam tree.
# 4. Mengulangi proses sampai semua node terhubung.
#
# Program menggunakan heapq agar pencarian
# bobot minimum menjadi lebih cepat.
#
# Edge yang dipilih:
# - A ke C = 2
# - C ke D = 1
# - D ke B = 3
#
# Total bobot MST:
# 2 + 1 + 3 = 6
#
# Hasil tersebut menunjukkan bahwa seluruh node
# dapat terhubung dengan biaya minimum
# tanpa membentuk cycle.


# ======================================================
# Hasil Diskusi
# ======================================================
# Dari hasil pengamatan program,
# algoritma Prim membangun MST secara bertahap
# mulai dari satu node awal.
#
# Perbedaan utama Prim dan Kruskal:
# - Prim fokus pada pengembangan node.
# - Kruskal fokus pada pemilihan edge global.
#
# Kelebihan Prim:
# - Cocok untuk dense graph.
# - Efisien jika menggunakan priority queue.
#
# Kekurangan Prim:
# - Membutuhkan node awal.
# - Implementasi sedikit lebih kompleks
#   dibandingkan Kruskal sederhana.
#
# Kesimpulan:
# Algoritma Prim efektif digunakan untuk
# optimasi jaringan karena dapat membentuk
# koneksi minimum secara bertahap dan efisien.