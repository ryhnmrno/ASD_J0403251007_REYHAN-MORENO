# ==========================================
# Program: Pencarian pada Doubly Linked List
# Mata Kuliah: Algoritma dan Struktur Data
# Nama: Reyhan Moreno
# NIM: J0403251007
# Kelas: B2
# ==========================================

# Kelas Node untuk Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data      # Data node
        self.next = None      # Pointer ke node berikutnya
        self.prev = None      # Pointer ke node sebelumnya


# Kelas Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Head menunjuk node pertama

    # Method untuk menambahkan node di akhir list
    def append(self, data):
        new_node = Node(data)

        # Jika list kosong
        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        
        temp.next = new_node
        new_node.prev = temp

    # Method untuk mencari elemen dalam list
    def search(self, key):
        temp = self.head

        # Traversal untuk mencari nilai
        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    # Method untuk menampilkan isi list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("null")


# ======================
# Program Utama
# ======================

dll = DoublyLinkedList()

input_data = input("Masukkan elemen ke dalam Doubly Linked List (pisahkan dengan koma): ")

if input_data.strip() == "":
    print("Doubly Linked List kosong. Tidak ada elemen yang bisa dicari.")
else:
    elements = list(map(int, input_data.split(",")))

    for el in elements:
        dll.append(el)

    print("Doubly Linked List:")
    dll.display()

    cari = int(input("Masukkan elemen yang ingin dicari: "))

    if dll.search(cari):
        print(f"Elemen {cari} ditemukan dalam Doubly Linked List.")
    else:
        print(f"Elemen {cari} tidak ditemukan dalam Doubly Linked List.")
