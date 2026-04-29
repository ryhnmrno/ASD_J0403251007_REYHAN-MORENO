#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Materi 2 : Implementasi BFS
#======================================================

# Struktur data untuk membuat antrian, kita gunakan dari library collections bawaan Phython
from collections import deque

#representasi graph 
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],        
    'G': []

}

def bfs(graph, start):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimpan struktur dari graph
    # start : node awal penelusuran
    
    #Queue digunakan untuk menyimpan node yang akan di proses / dibaca
    queue = deque()
    
    #variabel yang digunakan untuk menyimpan node yang sudah diproses / sudah dikunjungi
    visited = set()
    
    #masukkan node awal ke queue
    queue.append(start) #menambahkan node awal ke dalam antrian
    
    #tandai node awal sebagai node yang sudah dikunjungi
    visited.add(start) #menambahkan node awal ke dalam set visited
    
    while queue: 
        #mengambil node paling depan dari queue
        node = queue.popleft() #mengambil node paling depan dari antrian
        
        print(node, end=' ') #menampilkan node yang sedang diproses
        
        #periksa semua tetangga dari node yang diambil
        for neighbor in graph[node]: #melakukan iterasi untuk setiap tetangga dari node yang diambil
            if neighbor not in visited: #jika tetangga belum dikunjungi
                visited.add(neighbor) #tandai tetangga sebagai node yang sudah dikunjungi
                queue.append(neighbor) #tambahkan tetangga ke dalam antrian
                

# pemanggilan fungsi
bfs(graph, 'A')