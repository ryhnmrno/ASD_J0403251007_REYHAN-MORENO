# ==========================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2  
# Latihan 6 : Rotasi Kanan pada BST Tidak Seimbang 
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
    # fungsi untuk melihat bentuk tree
    if root is not None: 
        print("   " * level + f"{posisi}: {root.data}") 
        tampil_struktur(root.left, level + 1, "L")   # tampilkan kiri
        tampil_struktur(root.right, level + 1, "R")  # tampilkan kanan


# Fungsi rotasi kanan 
def rotate_right(y): 
    # y adalah root lama
    
    x = y.left        # x adalah child kiri (akan jadi root baru)
    T2 = x.right      # subtree kanan milik x disimpan sementara

    # Proses rotasi:
    x.right = y       # y dipindah jadi child kanan dari x
    y.left = T2       # subtree T2 jadi child kiri dari y

    # x menjadi root baru
    return x


# ----------------------------- 
# Program utama 
# ----------------------------- 

# Membuat tree yang tidak seimbang:
# 30 -> 20 -> 10 (condong ke kiri)
root = Node(30) 
root.left = Node(20) 
root.left.left = Node(10) 

print("Preorder sebelum rotasi kanan:") 
preorder(root) 

print("\n\nStruktur sebelum rotasi kanan:") 
tampil_struktur(root) 

# Melakukan rotasi kanan pada root
root = rotate_right(root) 

print("\nPreorder sesudah rotasi kanan:") 
preorder(root) 

print("\n\nStruktur sesudah rotasi kanan:") 
tampil_struktur(root) 


# Kesimpulan:
# setelah saya pahami, program ini melakukan rotasi kanan untuk memperbaiki tree yang condong ke kiri
# awalnya bentuknya 30 → 20 → 10, lalu setelah rotasi root berubah jadi 20
# node 10 jadi kiri dan 30 jadi kanan, sehingga tree lebih seimbang
# rotasi kanan membantu menjaga performa BST agar tidak memanjang ke satu arah