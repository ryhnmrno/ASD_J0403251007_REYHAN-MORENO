#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 3 : Implementasi Algoritma Prim
#======================================================

# Import library heapq
# Digunakan untuk priority queue
import heapq

# Representasi graph berbobot
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # Menyimpan edge sementara
    edges = []

    # Memasukkan edge awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # Menyimpan hasil MST
    mst = []

    # Menyimpan total bobot
    total_weight = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            # Menambahkan node ke visited
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan total bobot
            total_weight += weight

            # Menambahkan edge baru ke heap
            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight

# Menjalankan fungsi prim
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total)

# ======================================================
# Jawaban Analisis:
# 1. Node awal yang digunakan adalah A.
#
# 2. Edge pertama yang dipilih adalah A-C karena
#    memiliki bobot terkecil dari node A.
#
# 3. Prim menentukan edge berikutnya dengan memilih
#    edge minimum yang terhubung dengan node yang
#    sudah dikunjungi.
#
# 4. Total bobot MST yang dihasilkan adalah 6.
#
# 5. Perbedaan Prim dan Kruskal adalah Prim dimulai
#    dari node awal lalu memperbesar tree, sedangkan
#    Kruskal memilih edge minimum secara global.
# ======================================================