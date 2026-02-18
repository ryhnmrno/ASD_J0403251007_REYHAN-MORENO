#====================================
#Nama   : Reyhan Moreno
#NIM    : J0403251007
#Kelas  : TPL B2
#====================================

#====================================
#Impelementasi Dasar : Node pada Linked List
#====================================

class Node:
    def __init__(self, data): #konstruktor untuk inisialisasi node
        self.data = data #menyimpan nilai data
        self.next = None #pointer ke node berikutnya

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self, data):
        #Menambah data di belakang (tail)
        nodeBaru = Node(data)

        #Jika queue kosong, front dan rear menunjuk ke node yang sama
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return
        #Rear pindah ke node baru
        self.rear.next = nodeBaru
        self.rear = nodeBaru
        
    def dequeue(self):
        #Menghapus data dari depan 
        
        #1)lihat data yang paling depan
        data_terhapus = self.front.data #Simpan data yang akan dihapus
        
        #2)geser front ke node berikutnya
        self.front = self.front.next
        
        #3) jika setelah geser front menjadi None, berarti queue kosong
        #rear juga harus jadi None
        if self.front is None: #Jika setelah dihapus queue menjadi kosong, rear juga harus diupdate
            self.rear = None
            
        return data_terhapus #Kembalikan data yang dihapus
        
        
    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front", end=" -> ")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear di node terakhir")

#Instantiasi objek class queuell
q=QueueLL()
q.enqueue("A")
q.enqueue("B")
q.enqueue("C")
q.tampilkan()

q.dequeue()
q.tampilkan()