#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 3 : Membuat Traversal Preorder
#======================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#Fungsi preorder : Root -> Left -> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") #fix di sini
        preorder(node.left)
        preorder(node.right)

#membuat tree
#Membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan fungsi preorder
print("Traversal Preorder:")    
preorder(root) #output: A B D E C

#Penjelasan:
'''
Setelah saya pahami, program ini menerapkan traversal preorder pada tree yang sudah dibentuk,
dengan urutan Root -> Left -> Right. Proses dimulai dari node "A", lalu ke subtree kiri ("B", "D", "E"),
dan terakhir subtree kanan ("C"). Output ditampilkan secara berurutan dalam satu baris menggunakan
end=" " agar hasil traversal terlihat rapi sesuai urutan kunjungan node.
'''