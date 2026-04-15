#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 2 : Struktur organisasi Perusahaan
#======================================================

#class node digunakan untuk dasar dari tree
class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#fungsi preorder : Root -> Left -> Right
def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)

#membuat tree struktur organisasi 
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Staff 1")
root.left.right = Node("Staff 2")

root.right.left = Node("Staff 3")

#menjalankan traversal preorder
print("Struktur Organisasi (preorder):")
preorder(root) #output: Direktur Manajer A Staff 1 Staff 2 Manajer B Staff 3

#Penjelasan:
'''
Setelah saya pahami, program ini merepresentasikan struktur organisasi perusahaan menggunakan konsep tree
dengan class Node di Python, di mana setiap node berisi data serta memiliki pointer left dan right untuk
menghubungkan hubungan atasan dan bawahan. Root dari tree ini adalah "Direktur", kemudian memiliki dua
manajer yaitu "Manajer A" dan "Manajer B". Selanjutnya, "Manajer A" memiliki dua staff yaitu "Staff 1"
dan "Staff 2", sedangkan "Manajer B" memiliki satu staff yaitu "Staff 3". Program kemudian menjalankan
traversal preorder (Root -> Left -> Right) untuk menampilkan urutan hierarki organisasi mulai dari direktur
hingga seluruh staff secara berurutan dalam satu baris menggunakan end=" ".
'''