# ==========================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2 
# Latihan 5 : Rotasi Kiri pada BST Tidak Seimbang 
# ========================================================== 

# Class Node 
class Node: 
    def __init__(self, data): 
        self.data = data          # menyimpan nilai node
        self.left = None          # child kiri
        self.right = None         # child kanan


# Fungsi preorder untuk melihat isi tree 
def preorder(root): 
    # preorder: Root → Kiri → Kanan
    if root is not None: 
        print(root.data, end=" ")     # tampilkan root
        preorder(root.left)          # ke kiri
        preorder(root.right)         # ke kanan


# Fungsi untuk menampilkan struktur tree 
def tampil_struktur(root, level=0, posisi="Root"): 
    # fungsi untuk melihat bentuk tree secara sederhana
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        # spasi menyesuaikan level supaya terlihat bentuknya
        
        tampil_struktur(root.left, level + 1, "L")   # tampilkan kiri
        tampil_struktur(root.right, level + 1, "R")  # tampilkan kanan


# Fungsi rotasi kiri 
def rotate_left(x): 
    # x adalah root lama 
    
    y = x.right       # y adalah child kanan x (akan jadi root baru)
    T2 = y.left       # subtree kiri milik y disimpan sementara 

    # Proses rotasi:
    # langkah ini mengubah struktur tree
    y.left = x        # x dipindah jadi child kiri dari y 
    x.right = T2      # subtree T2 dipindah jadi child kanan x 

    # y sekarang jadi root baru
    return y 



# ----------------------------- 
# Program utama 
# ----------------------------- 

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30 (condong ke kanan)
root = Node(10) 
root.right = Node(20) 
root.right.right = Node(30) 

print("Preorder sebelum rotasi kiri:") 
preorder(root) 

print("\n\nStruktur sebelum rotasi kiri:") 
tampil_struktur(root) 

# Melakukan rotasi kiri pada root
root = rotate_left(root) 

print("\nPreorder sesudah rotasi kiri:") 
preorder(root) 

print("\n\nStruktur sesudah rotasi kiri:") 
tampil_struktur(root) 


# Penjelasan:
# setelah saya pahami, program ini melakukan rotasi kiri untuk memperbaiki tree yang tidak seimbang
# awalnya tree condong ke kanan (10 → 20 → 30), lalu setelah rotasi root berubah menjadi 20
# node 10 jadi child kiri dan 30 tetap di kanan, sehingga tree lebih seimbang
# rotasi kiri ini penting untuk menjaga performa BST agar tidak menjadi seperti linked list