#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 4 : Studi Kasus: Jaringan Kabel Antar Gedung
#======================================================

# Mengimpor library heapq untuk membantu mengambil
# nilai edge dengan bobot terkecil secara otomatis
import heapq

# Membuat representasi weighted graph menggunakan dictionary
# Format:
# 'Node': {'Tetangga': bobot}
graph = {
    'GedungA': {'GedungB': 4, 'GedungC': 2, 'GedungD': 5},
    'GedungB': {'GedungA': 4, 'GedungD': 3},
    'GedungC': {'GedungA': 2, 'GedungD': 1},
    'GedungD': {'GedungA': 5, 'GedungB': 3, 'GedungC': 1}
}

# Membuat fungsi prim()
# Fungsi ini digunakan untuk mencari
# Minimum Spanning Tree (MST)
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # List untuk menyimpan kandidat edge
    edges = []

    # List untuk menyimpan hasil MST
    mst = []

    # Variabel untuk menghitung total biaya
    total_cost = 0

    # Mengambil semua tetangga dari node awal
    for neighbor, weight in graph[start].items():

        # Memasukkan edge ke priority queue
        # Format: (bobot, node_asal, node_tujuan)
        heapq.heappush(edges, (weight, start, neighbor))

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sebagai sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total biaya
            total_cost += weight

            # Mengecek tetangga dari node baru
            for neighbor, w in graph[v].items():

                # Jika tetangga belum dikunjungi
                if neighbor not in visited:

                    # Menambahkan edge baru ke priority queue
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total biaya
    return mst, total_cost


# Memanggil fungsi prim()
# Dimulai dari node GedungA
mst, total = prim(graph, 'GedungA')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total)


# ======================================================
# Penjelasan Program
# ======================================================
# Program ini digunakan untuk menentukan jaringan kabel
# internet antar gedung dengan biaya minimum menggunakan
# algoritma Prim.
#
# Algoritma Prim bekerja dengan cara:
# 1. Memulai dari satu node awal.
# 2. Memilih edge dengan bobot terkecil.
# 3. Menambahkan node baru ke dalam tree.
# 4. Menghindari cycle atau pengulangan jalur.
# 5. Mengulangi proses sampai semua node terhubung.
#
# Pada program ini digunakan priority queue dari heapq
# agar pencarian bobot terkecil menjadi lebih cepat.
#
# Hasil MST:
# GedungA -> GedungC = 2
# GedungC -> GedungD = 1
# GedungD -> GedungB = 3
#
# Total biaya minimum:
# 2 + 1 + 3 = 6


# ======================================================
# Jawaban Analisis
# ======================================================
# 1. Algoritma apa yang digunakan?
# Jawab:
# Program ini menggunakan algoritma Prim.
#
# 2. Edge mana saja yang dipilih?
# Jawab:
# Edge yang dipilih yaitu:
# - GedungA ke GedungC = 2
# - GedungC ke GedungD = 1
# - GedungD ke GedungB = 3
#
# 3. Berapa total biaya minimum?
# Jawab:
# Total biaya minimum adalah 6.
#
# 4. Mengapa MST cocok digunakan pada kasus ini?
# Jawab:
# Karena MST dapat menghubungkan semua gedung
# dengan biaya kabel paling kecil tanpa membuat
# jalur yang berulang atau cycle sehingga
# pemasangan jaringan menjadi lebih efisien.