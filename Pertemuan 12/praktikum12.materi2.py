#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Materi 2 : Implementasi Algoritma Bellman-Ford
#======================================================

# Membuat graph berbobot (bisa sama seperti contoh Dijkstra)
# Format: node : {tetangga: bobot}
graph = {
    'A': {'B': 4, 'C': 2},   # A ke B = 4, A ke C = 2
    'B': {'D': 5},           # B ke D = 5
    'C': {'D': 1},           # C ke D = 1
    'D': {}                  # D tidak punya tetangga
}

# Fungsi Bellman-Ford
def bellman_ford(graph, start):
    
    # Inisialisasi semua jarak ke tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Set jarak node awal ke dirinya sendiri = 0
    distances[start] = 0
    
    # Proses relaksasi dilakukan sebanyak (jumlah node - 1)
    # Tujuannya untuk memastikan semua jalur terpendek ditemukan
    for _ in range(len(graph) - 1):
        
        # Loop semua node dalam graph
        for node in graph:
            
            # Loop semua tetangga dari node tersebut
            for neighbor, weight in graph[node].items():
                
                # Hitung kemungkinan jarak baru
                # (jarak node sekarang + bobot ke tetangga)
                if distances[node] + weight < distances[neighbor]:
                    
                    # Jika lebih kecil, update jarak
                    distances[neighbor] = distances[node] + weight
    
    # Mengembalikan hasil jarak terpendek
    return distances

# Memanggil fungsi dengan node awal 'A'
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")

# Menampilkan semua node dan jaraknya
for node, distance in hasil.items():
    print(node, "=", distance)

# =========================
# Penjelasan:
# Algoritma Bellman-Ford digunakan untuk mencari jarak terpendek
# dari satu node ke semua node lain.
#
# Perbedaannya dengan Dijkstra:
# - Bellman-Ford melakukan relaksasi berulang pada semua edge
# - Bisa digunakan untuk graph dengan bobot negatif
#
# Pada contoh ini:
# A ke B = 4
# A ke C = 2
# A ke D = 3 (melalui C karena lebih kecil)
#
# Proses relaksasi memastikan bahwa setiap kemungkinan jalur
# sudah dicek dan jarak yang didapat benar-benar minimum.
# =========================