#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Materi 3 : Implementasi DFS
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

def dfs(graph, node, visited):
    # Fungsi untuk melakukan penelusuran graph dengan BFS
    # graph : dictionary yang menyimpan struktur dari graph
    # node : menyimpan node yang sedang dikunjungi
    # visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node) #menambahkan node saat ini ke dalam set visited

    #tampilkan node yang sedang dikunjungi
    print(node, end=' ') #menampilkan node yang sedang diproses

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:
        
        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            dfs(graph, neighbor, visited) #lakukan penelusuran DFS untuk tetangga tersebut
            
#set visited
visited = set() #membuat set kosong untuk menyimpan node yang sudah dikunjungi

#menjalankan DFS dari A
dfs(graph, 'A', visited) #memanggil fungsi DFS dengan node awal A dan set visited yang kosong