# ==========================================
# Program: Menghapus Node pada Single Linked List
# Mata Kuliah: Algoritma dan Struktur Data
# Nama: Reyhan Moreno
# NIM: J0403251007
# Kelas: B2
# ==========================================

# Kelas Node untuk menyimpan data dan pointer next
class Node:
    def __init__(self, data):
        self.data = data      # Data yang disimpan dalam node
        self.next = None      # Pointer ke node berikutnya


# Kelas Single Linked List
class SingleLinkedList:
    def __init__(self):
        self.head = None      # Head menunjuk ke node pertama

    # Method untuk menambahkan node di akhir list
    def append(self, data):
        new_node = Node(data)

        # Jika list kosong, node baru menjadi head
        if not self.head:
            self.head = new_node
            return
        
        # Jika tidak kosong, telusuri sampai node terakhir
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Method untuk menghapus node berdasarkan nilai (key)
    def delete_node(self, key):
        temp = self.head

        # Jika node yang ingin dihapus adalah head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None

        # Mencari node dengan nilai yang sesuai
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        # Jika nilai tidak ditemukan
        if temp is None:
            print("Elemen tidak ditemukan.")
            return

        # Menghapus node dengan mengubah pointer
        prev.next = temp.next
        temp = None

    # Method untuk menampilkan isi linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")


# ======================
# Program Utama
# ======================

sll = SingleLinkedList()
data = [1, 3, 5, 7, 9]

# Menambahkan data awal ke linked list
for item in data:
    sll.append(item)

print("Linked List sebelum dihapus:")
sll.display()

hapus = int(input("Masukkan elemen yang ingin dihapus: "))
sll.delete_node(hapus)

print("Linked List setelah dihapus:")
sll.display()
