#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 5 : Membuat Traversal Postorder
#======================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat fungsi postorder : Left -> Right -> Root
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ") #fix di sini

#membuat tree
#Membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menjalankan fungsi postorder
print("Traversal Postorder:")
postorder(root) #output: D E B C A

#Penjelasan:
'''
Setelah saya pahami, program ini menerapkan traversal postorder pada struktur data tree menggunakan Python,
dengan class Node sebagai pembentuk node yang memiliki atribut data, left, dan right. Tree dibangun dengan
root bernilai "A", kemudian memiliki child "B" dan "C", serta "D" dan "E" sebagai child dari node "B".
Selanjutnya fungsi postorder menjalankan penelusuran dengan urutan Left -> Right -> Root, yaitu mengunjungi
seluruh cabang terlebih dahulu sebelum node utama diproses. Hasil output ditampilkan secara berurutan dalam
satu baris menggunakan end=" " agar sesuai dengan urutan traversal postorder.
'''
