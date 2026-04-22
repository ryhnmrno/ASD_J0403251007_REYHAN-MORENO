#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 1 : Node dan Insert BST
#======================================================

class Node:
    def __init__(self, data):
        self.data = data        # menyimpan nilai/data pada node
        self.left = None        # child kiri (untuk nilai yang lebih kecil)
        self.right = None       # child kanan (untuk nilai yang lebih besar)
        
def insert(root, data):
    # fungsi untuk memasukkan data ke dalam BST
    
    # kalau root masih kosong, langsung buat node baru
    if root is None:
        return Node(data)
    
    # kalau data lebih kecil dari root, masuk ke kiri
    if data < root.data:
        # proses ini akan terus berulang (rekursif) sampai nemu tempat kosong
        root.left = insert(root.left, data)
    
    # kalau data lebih besar dari root, masuk ke kanan
    elif data > root.data:
        root.right = insert(root.right, data)
    
    # kalau datanya sama, tidak dimasukkan (diabaikan)
    
    # return root supaya struktur tree tetap nyambung
    return root


# mengisi data BST
root = None   # awalnya belum ada isi (kosong)

data_list = [50, 30, 70, 20, 40, 50, 80]

# perulangan untuk memasukkan semua data ke BST
for data in data_list:
    root = insert(root, data)
    # setiap data dimasukkan satu per satu sesuai aturan BST

print("BST berhasil dibuat")


#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 2 : Traversal Inorder
#======================================================

def inorder(root): 
    # traversal inorder: kiri → root → kanan
    if root is not None:
        inorder(root.left)          # pertama ke kiri dulu sampai habis
        print(root.data, end=' ')   # lalu cetak data di node sekarang
        inorder(root.right)         # terakhir ke kanan

# hasil traversal inorder di BST pasti urut dari kecil ke besar
print("Hasil Inorder:")
inorder(root)


#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 3 : Search BST
#======================================================

def search(root, key):
    # fungsi untuk mencari data di BST
    
    # kalau node kosong, berarti data tidak ada
    if root is None:
        return False
    
    # kalau data ditemukan
    if root.data == key:
        return True
    
    # kalau key lebih kecil, cari ke kiri
    elif key < root.data:
        return search(root.left, key)
    
    # kalau key lebih besar, cari ke kanan
    else:
        return search(root.right, key)

# uji pencarian
key = 40

# mulai pencarian dari root
if search(root, key):
    print("Data Ditemukan")
else:
    print("Data Tidak Ditemukan")


# Penjelasan:
# setelah saya pahami, program ini digunakan untuk membuat BST, menampilkan data secara terurut
# menggunakan inorder, dan melakukan pencarian data dengan lebih efisien
# proses insert menentukan posisi node berdasarkan aturan kiri < root < kanan
# inorder menghasilkan data terurut, sedangkan search mempercepat pencarian tanpa cek semua data
# jika data tidak ada (seperti 100), maka akan berhenti saat node kosong