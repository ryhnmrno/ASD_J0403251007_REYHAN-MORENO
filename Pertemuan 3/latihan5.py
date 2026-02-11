# ==========================================
# Program: Reverse Single Linked List
# Mata Kuliah: Algoritma dan Struktur Data
# Nama: Reyhan Moreno
# NIM: J0403251007
# Kelas: B2
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node di akhir list
    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # Membalik linked list tanpa membuat list baru
    def reverse(self):
        prev = None
        current = self.head

        # Proses pembalikan arah pointer
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    # Menampilkan isi list
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

input_data = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")

if input_data.strip() == "":
    print("Linked List kosong.")
else:
    elements = list(map(int, input_data.split(",")))

    for el in elements:
        sll.append(el)

    print("Linked List sebelum dibalik:")
    sll.display()

    sll.reverse()

    print("Linked List setelah dibalik:")
    sll.display()
