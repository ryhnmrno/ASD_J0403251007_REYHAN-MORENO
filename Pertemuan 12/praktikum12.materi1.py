#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Materi 1 : Implementasi Algoritma Dijkstra
#======================================================

import heapq  # digunakan untuk membuat priority queue (antrian prioritas)

# Representasi graph dalam bentuk dictionary
# Setiap node memiliki tetangga dan bobot (weight/jarak)
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Inisialisasi semua jarak node = tak hingga (infinity)
    distances = {node: float('inf') for node in graph}
    
    # Jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0
    
    # Priority queue untuk menyimpan (jarak, node)
    pq = [(0, start)]
    
    # Selama masih ada node di dalam queue
    while pq:
        # Ambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)
        
        # Periksa semua tetangga dari node sekarang
        for neighbor, weight in graph[current_node].items():
            
            # Hitung jarak baru
            distance = current_distance + weight
            
            # Jika jarak baru lebih kecil dari sebelumnya
            if distance < distances[neighbor]:
                distances[neighbor] = distance  # update jarak
                
                # Masukkan ke priority queue
                heapq.heappush(pq, (distance, neighbor))
    
    # Mengembalikan hasil jarak terpendek ke semua node
    return distances

# Memanggil fungsi dijkstra dari node 'A'
hasil = dijkstra(graph, 'A')

# Menampilkan hasil
print(hasil)

# Setelah saya membaca dan memahami bahwa algoritma Dijkstra digunakan untuk mencari jarak terpendek dari satu titik ke titik lain dalam graph.
# Pertama, semua jarak di-set ke tak hingga, karena belum diketahui jaraknya.
# Node awal (A) di-set ke 0 karena jarak ke dirinya sendiri adalah 0.
# Menggunakan priority queue supaya node dengan jarak terkecil diproses lebih dulu.
# Setiap node akan dicek tetangganya:
# Jika ditemukan jalur yang lebih pendek, maka jaraknya di-update.
# Proses ini diulang sampai semua node sudah diproses.