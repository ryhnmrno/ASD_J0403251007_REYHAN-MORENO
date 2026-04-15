    #======================================================
    # Nama : Reyhan Moreno
    # NIM : J0403251007
    # Kelas : B2
    # Latihan 2 : Membuat node tree
    #======================================================

    #class node digunakan untuk dasar dari tree

class Node:
    def __init__(self, data):
        self.data = data #menyimpan nilai node
        self.left = None #child kiri
        self.right = None #child kanan

#membuat tree
#Membuat sebuah node root
root = Node("A")

#membuat child level 1
root.left = Node("B")
root.right = Node("C")

#membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")

#menampilkan isi node
print("Data pada root:", root.data) #output: A
print("Data childkiri root:", root.left.data) #output: B
print("Data childkanan root:", root.right.data) #output: C
print("Data childkiri dari B :", root.left.left.data) #output:
print("Data childkanan dari B :", root.left.right.data) #output: E

#Penjelasan:
'''
Setelah saya pahami, program ini membentuk struktur tree sederhana dengan membuat root "A", lalu
menambahkan child "B" dan "C" pada level pertama, serta "D" dan "E" sebagai child dari node "B".
Program ini menunjukkan hubungan parent-child dalam tree dan bagaimana node saling terhubung
secara hierarki, kemudian menampilkan isi setiap node berdasarkan strukturnya.
'''