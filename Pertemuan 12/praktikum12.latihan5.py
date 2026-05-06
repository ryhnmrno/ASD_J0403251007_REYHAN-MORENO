#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 5 : Jalur Terpendek Antar Kota
#======================================================

import heapq  # digunakan untuk priority queue

# Membuat graph kota
# Bobot menunjukkan jarak antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},   # dari Bogor ke Jakarta 5, ke Depok 2
    'Depok': {'Jakarta': 2, 'Bandung': 6}, # dari Depok ke Jakarta 2, ke Bandung 6
    'Jakarta': {'Bandung': 7},              # dari Jakarta ke Bandung 7
    'Bandung': {}                          # Bandung tujuan akhir
}

# Fungsi Dijkstra
def dijkstra(graph, start):
    
    # Inisialisasi jarak semua kota = tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Set jarak awal = 0
    distances[start] = 0
    
    # Membuat priority queue
    pq = [(0, start)]
    
    # Selama queue masih ada
    while pq:
        
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)
        
        # Periksa semua tetangga
        for neighbor, weight in graph[current_node].items():
            
            # Hitung jarak baru
            distance = current_distance + weight
            
            # Jika lebih kecil, update
            if distance < distances[neighbor]:
                
                distances[neighbor] = distance
                
                # Masukkan ke queue
                heapq.heappush(pq, (distance, neighbor))
    
    # Kembalikan hasil
    return distances

# Jalankan dari Bogor
hasil = dijkstra(graph, 'Bogor')

# Menampilkan hasil
print("Jarak terpendek dari Bogor:")

# Loop hasil
for kota, jarak in hasil.items():
    print("Bogor ->", kota, "=", jarak)

# =========================
# Jawaban Analisis:
# 1. Node awal yang digunakan adalah Bogor, karena menjadi titik awal pencarian
#    jarak ke kota lain.
#
# 2. Kota dengan jarak paling kecil adalah Depok (2), karena merupakan jalur
#    langsung dengan bobot terkecil dari Bogor.
#
# 3. Kota dengan jarak paling besar adalah Bandung (8), karena harus melalui
#    beberapa node, misalnya Bogor -> Depok -> Bandung (2 + 6 = 8).
#
# 4. Algoritma Dijkstra bekerja dengan memilih jalur dengan jarak terkecil terlebih dahulu,
#    kemudian memperbarui jarak ke node lain secara bertahap sampai semua jarak optimal ditemukan.
# =========================