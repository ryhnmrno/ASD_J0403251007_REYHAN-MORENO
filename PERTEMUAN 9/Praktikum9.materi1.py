#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
# Latihan 1 : Membuat node 
#======================================================

#class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat root
root = Node("A")

#menampilkan isi node
print("Data pada root:", root.data) #output: A
print("Data childkiri root:", root.left) #output: None
print("Data childkanan root:", root.right) #output: None

#Penjelasan:
'''
Setelah saya pahami, program ini membuat dasar struktur data tree menggunakan class Node di Python,
di mana dibuat satu node root bernilai "A" yang memiliki atribut left dan right namun masih bernilai
None karena belum memiliki child. Program kemudian menampilkan isi root serta kondisi child kiri dan
kanan yang masih kosong, sehingga menunjukkan bahwa node tersebut berdiri sendiri tanpa cabang.
'''