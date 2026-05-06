#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 3 : Implementasi Bellman-Ford
#======================================================

# Graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},   # A ke B dan C
    'B': {},                 # B kosong
    'C': {'B': -2}           # C ke B dengan bobot negatif
}

# Fungsi Bellman-Ford
def bellman_ford(graph, start):
    
    # Inisialisasi jarak
    distances = {node: float('inf') for node in graph}
    
    # Set node awal
    distances[start] = 0
    
    # Relaksasi sebanyak n-1
    for _ in range(len(graph) - 1):
        
        # Loop semua node
        for node in graph:
            
            # Loop semua tetangga
            for neighbor, weight in graph[node].items():
                
                # Jika jarak valid dan lebih kecil
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    
                    # Update jarak
                    distances[neighbor] = distances[node] + weight
    
    # Kembalikan hasil
    return distances

# Memanggil fungsi
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")

# Loop hasil
for node, distance in hasil.items():
    print(node, "=", distance)

# =========================
# Jawaban Analisis:
# 1. Bobot langsung dari A ke B adalah 5.
#
# 2. Total bobot jalur A -> C -> B adalah 2, yaitu dari 4 + (-2).
#
# 3. Jalur yang menghasilkan jarak lebih kecil adalah melalui C,
#    karena totalnya lebih kecil dibandingkan jalur langsung.
#
# 4. Bellman-Ford dapat digunakan pada graph dengan bobot negatif karena
#    algoritma ini melakukan relaksasi berulang pada semua edge,
#    sehingga tetap bisa menemukan jalur terpendek secara benar.
#
# 5. Relaksasi edge adalah proses memperbarui nilai jarak jika ditemukan
#    jalur yang lebih pendek dari sebelumnya.
#
# 6. Perbedaan utama adalah Dijkstra lebih cepat tetapi tidak bisa menangani
#    bobot negatif, sedangkan Bellman-Ford lebih lambat tetapi lebih fleksibel
#    karena bisa digunakan pada graph dengan bobot negatif.
# =========================