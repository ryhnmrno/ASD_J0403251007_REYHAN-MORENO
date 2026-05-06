#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 4 : Jalur Terpendek Lokasi Kampus 
#======================================================

import heapq  # digunakan untuk membuat priority queue (antrian prioritas)

# Membuat graph lokasi kampus
# Setiap node adalah lokasi, dan bobot menunjukkan waktu tempuh (menit)
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},  # dari Gerbang ke Perpustakaan 6 menit, ke Kantin 2 menit
    'Perpustakaan': {'Lab': 3},                   # dari Perpustakaan ke Lab 3 menit
    'Kantin': {'Lab': 4, 'Aula': 7},              # dari Kantin ke Lab 4 menit, ke Aula 7 menit
    'Lab': {'Aula': 1},                           # dari Lab ke Aula 1 menit
    'Aula': {}                                    # Aula tidak punya tujuan lagi
}

# Fungsi Dijkstra untuk mencari jarak tercepat
def dijkstra(graph, start):
    
    # Inisialisasi semua jarak ke tak hingga
    distances = {node: float('inf') for node in graph}
    
    # Set jarak dari node awal ke dirinya sendiri = 0
    distances[start] = 0
    
    # Membuat priority queue berisi (jarak, node)
    priority_queue = [(0, start)]
    
    # Selama masih ada data di queue
    while priority_queue:
        
        # Ambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Jika jarak saat ini lebih besar dari data yang sudah ada, lewati
        if current_distance > distances[current_node]:
            continue
        
        # Periksa semua tetangga dari node sekarang
        for neighbor, weight in graph[current_node].items():
            
            # Hitung jarak baru ke tetangga
            distance = current_distance + weight
            
            # Jika jarak lebih kecil dari sebelumnya
            if distance < distances[neighbor]:
                
                # Update jarak
                distances[neighbor] = distance
                
                # Masukkan ke queue untuk diproses lagi
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Kembalikan semua hasil jarak
    return distances

# Menjalankan algoritma dari Gerbang
hasil = dijkstra(graph, 'Gerbang')

# Menampilkan hasil
print("Jarak terpendek dari Gerbang:")

# Loop semua lokasi dan jaraknya
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

# =========================
# Jawaban Analisis:
# 1. Lokasi yang paling dekat dari Gerbang adalah Kantin dengan waktu 2 menit,
#    karena memiliki bobot paling kecil dibandingkan jalur lainnya.
#
# 2. Waktu tercepat ke Aula adalah 7 menit, melalui jalur:
#    Gerbang -> Kantin -> Lab -> Aula (2 + 4 + 1 = 7).
#    Walaupun ada jalur langsung dari Kantin ke Aula (7), jalur lewat Lab tetap optimal.
#
# 3. Jalur langsung tidak selalu paling cepat, karena bisa saja jalur tidak langsung
#    memiliki total bobot yang lebih kecil. Jadi harus dihitung semua kemungkinan.
#
# 4. Dijkstra cocok digunakan karena semua bobot bernilai positif,
#    sehingga algoritma bisa bekerja dengan optimal tanpa kesalahan perhitungan.
# =========================