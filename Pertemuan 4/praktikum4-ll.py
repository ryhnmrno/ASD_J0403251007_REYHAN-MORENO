#===================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : TPL B2
#===================================================

#===================================================
#Implementasi Dasar : Node pada Linked List
#===================================================

#membuat class node (merupakan unit dasar dari linked list)
class Node:
    def __init__(self, data): #Konstruktor
        self.data = data #Menyimpan nilai/data
        self.next = None #Pointer ke note berikutnya (awal=none)

# 1) Membuat node satu per satu
NodeA = Node("A")
NodeB = Node("B")
NodeC = Node("C")

# 2) Menghubungkan node : A -> B -> C -> None
NodeA.next = NodeB
NodeB.next = NodeC

# 3) Menentukan node pertama(head)  
head = NodeA

# 4) Traversal : menelusuri dari head sampai none
current = head 
while current is not None:
    print(current.data) #Menampilkan data pada node saat ini
    current = current.next #Pindah ke node berikutnya

#===================================================
#Implementasi Dasar : Linked List + Insert Awal
#===================================================

class LinkedList:
    def __init__(self):
        self.head = None #Inisialisasi head sebagai None (kosong)
    def insert_awal(self, data):
        #1) buat node baru
        nodeBaru = Node(data) #Panggil class node
        
        #2) node baru menunjuk head lama
        nodeBaru.next = self.head
        
        #3) head pindah ke node baru
        self.head = nodeBaru
    def hapus_awal(self):
        if self.head is None:
            print("Tidak ada node untuk dihapus")
            return
        data_terhapus = self.head.data #Simpan data yang akan dihapus
        self.head = self.head.next #Pindah head ke node berikutnya
        print("node yang dihapus:", data_terhapus) #Tampilkan data yang dihapus

    def tampilkan(self): #implementasi traversal
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
                
print("=====List Baru=====")
ll = LinkedList() #instantiasi objek ke class linked list
ll.insert_awal("X")
ll.insert_awal("Y")
ll.insert_awal("Z") 
ll.hapus_awal() 
ll.tampilkan()

        