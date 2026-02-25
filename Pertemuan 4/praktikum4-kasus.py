#====================================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : TPL B2 
#====================================================================

#====================================================================
# Studi kasus : Sistem Antrian Layanan Akademik
# Implementasi Queue =>
# Enqueue : memindahkan pointer rear (nambah data baru dari belakang)
# Dequeue : memindahkan pointer front (menghapus data dari depan)
# Stack ==> Front -> C -> B -> A -> None 
# # Front -> A -> B > C -> Rear
#====================================================================

# 1) Mendefinisikan Node (Unit dasar linked list)
class Node:
    def __init__(self, nim, nama):   
        self.nim = nim              # Menyimpan NIM mahasiswa
        self.nama = nama            # Menyimpan Nama mahasiswa
        self.next = None            # Pointer ke node berikutnya


# 2) Mendefinisikan queue, terdiri dari front dan rear
class queueAkademik:
    def __init__(self):
        self.front = None           # Pointer ke data paling depan (yang akan dilayani pertama)
        self.rear = None            # Pointer ke data paling belakang (data terakhir masuk)

    def is_empty(self):
        #Ketika queue kosomg maka front = rear = none
        return self.front is None
    
    #menambahkan data baru ke bagian belakang (rear) => menambahkan antrian mahasiswa yang akan mengajukan layanan akademik
    def enqueue(self,nim,nama):

        nodeBaru = Node(nim, nama)   # Membuat node baru dari data nim dan nama

        #Jika data baru masuk dari queue yang kosong maka data baru = front = rear
        if self.is_empty():
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #Jika queue tidak kosong, maka data baru diletakkan setelah rear kemudian dijadikan sebagai rear
        self.rear.next = nodeBaru
        self.rear = nodeBaru
        
    #menghapus data paling depan (memberikan layanan akademik)
    def dequeue(self):

        # Mengecek apakah antrian kosong
        if self.is_empty():
            print("Antrian Kosong, Tidak ada Mahasiswa yang dilayani")
            return None
        
        #lihat data bagian  front, simpan di variabel data yang akan dihapus (dilayani)
        node_dilayani = self.front

        #geser pointer front ke next front
        self.front = self.front.next

        #jika front menjadi none(data antrian terakhir yang dilayani), maka front = rear = none
        if self.front is None:
            self.rear = None

        # Mengembalikan data mahasiswa yang sudah dilayani
        return node_dilayani
    
    def tampilkan(self):

        # Mengecek apakah antrian kosong sebelum ditampilkan
        if self.is_empty():
            print("Antrian masih kosong")
            return

        current = self.front     # Mulai dari data paling depan
        no = 1                   # Nomor urut antrian

        # Menelusuri setiap node sampai habis
        while current is not None :
            print(f"{no}. {current.nim} - {current.nama}")
            current = current.next   # Pindah ke node berikutnya
            no += 1                  # Tambah nomor urut


# 3) Program Utama

def main():

    #instantiasi queue
    q = queueAkademik()

    # Perulangan menu utama (berjalan terus sampai pilih keluar)
    while True:
        print("===== Sistem Antrian Akademik =====")
        print("1. Tambah Mahasiswa")
        print("2. Layani Mahasiswa")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilihan = input("Pilih Menu (1-4) : ").strip()

        # Jika memilih tambah mahasiswa
        if pilihan == "1":
            nim = input("Masukkan NIM : ").strip()
            nama = input("Masukkan Nama : ").strip()

            q.enqueue(nim,nama)
            print("Mahasiswa Berhasil Ditambahkan ke antrian")

        # Jika memilih layani mahasiswa (hapus dari depan)
        elif pilihan == "2":
            dilayani = q.dequeue()

            if dilayani is not None:
                print(f"Mahasiswa Dilayani : {dilayani.nim} - {dilayani.nama}")

        # Jika memilih melihat seluruh antrian
        elif pilihan == "3":
            q.tampilkan()   

        # Jika memilih keluar dari program
        elif pilihan == "4":
            print("Program Selesai. Terima kasih.")
            break

        # Jika input tidak sesuai pilihan menu
        else:
            print("Pilihan tidak valid!")

# 4) Penanda eksekusi file utama

if __name__ == "__main__":
    main()