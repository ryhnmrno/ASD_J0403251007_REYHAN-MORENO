#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 4 : Membuat Traversal Inorder
#======================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat fungsi indorder : Left -> Root -> Right
def inorder(node):
    if node is not None:
        inorder(node.left)
        print(node.data, end=" ") #fix di sini
        inorder(node.right)

#membuat tree
#Membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan fungsi inorder
print("Traversal Inorder:")
inorder(root) #output: D B E A C

#Penjelasan:
'''
Setelah saya pahami, program ini menerapkan traversal inorder pada tree dengan urutan Left -> Root -> Right.
Proses dimulai dari subtree kiri terlebih dahulu, kemudian node utama, dan terakhir subtree kanan. Pada tree
ini, urutan hasilnya adalah "D B E A C". Output ditampilkan dalam satu baris menggunakan end=" " agar sesuai
dengan urutan traversal inorder.
'''