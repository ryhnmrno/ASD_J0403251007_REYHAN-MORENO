#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 2 : Implementasi Dijkstra
#======================================================

import heapq  # import library priority queue

# Membuat graph berbobot
graph = {
    'A': {'B': 4, 'C': 2},   # A ke B dan C
    'B': {'D': 5},           # B ke D
    'C': {'D': 1},           # C ke D
    'D': {}                  # D kosong
}

# Fungsi Dijkstra
def dijkstra(graph, start):
    
    # Inisialisasi semua jarak = tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Jarak awal = 0
    distances[start] = 0
    
    # Membuat priority queue
    priority_queue = [(0, start)]
    
    # Selama queue tidak kosong
    while priority_queue:
        
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak lebih besar, skip
        if current_distance > distances[current_node]:
            continue
        
        # Loop semua tetangga
        for neighbor, weight in graph[current_node].items():
            
            # Hitung jarak baru
            distance = current_distance + weight
            
            # Jika lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                
                # Masukkan ke queue
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Kembalikan hasil
    return distances

# Memanggil fungsi
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")

# Loop hasil
for node, distance in hasil.items():
    print(node, "=", distance)

# =========================
# Jawaban Analisis:
# 1. Jarak terpendek dari A ke B adalah 4, karena langsung terhubung tanpa jalur lain
#    yang lebih kecil.
#
# 2. Jarak terpendek dari A ke C adalah 2, juga merupakan jalur langsung dengan bobot kecil.
#
# 3. Jarak terpendek dari A ke D adalah 3, yaitu melalui jalur A -> C -> D (2 + 1).
#
# 4. Jarak ke D lebih kecil melalui C karena total bobotnya hanya 3,
#    sedangkan jika melalui B hasilnya 9, sehingga algoritma memilih jalur yang lebih murah.
#
# 5. Fungsi priority_queue adalah untuk menyimpan node yang akan diproses
#    dan memastikan node dengan jarak terkecil diproses terlebih dahulu,
#    sehingga algoritma menjadi lebih efisien.
#
# 6. Dijkstra tidak cocok untuk bobot negatif karena menggunakan pendekatan greedy,
#    di mana keputusan awal dianggap final. Jika ada bobot negatif, bisa terjadi
#    perubahan jarak yang membuat hasil menjadi tidak akurat.
# =========================