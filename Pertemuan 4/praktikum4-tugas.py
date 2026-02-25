#====================================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : TPL B2 
#====================================================================

#====================================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
#====================================================================

# 1) Mendefinisikan Node (unit dasar linked list untuk pelanggan bengkel)
class NodeBengkel:
    def __init__(self, no, nama, servis):
        self.no = no             # Nomor antrian pelanggan
        self.nama = nama         # Nama pelanggan
        self.servis = servis     # Jenis servis yang diajukan
        self.next = None         # Pointer ke node berikutnya


# 2) Mendefinisikan queue bengkel, terdiri dari front dan rear
class QueueBengkel:
    def __init__(self):
        self.front = None        # Pointer ke pelanggan paling depan (yang akan dilayani pertama)
        self.rear = None         # Pointer ke pelanggan paling belakang (pelanggan terakhir masuk)
    
    # Menambahkan pelanggan baru ke antrian (rear)
    def enqueue(self, no, nama, servis):
        # TODO: Tambahkan data ke antrian
        pass

    # Melayani pelanggan di depan (dequeue)
    def dequeue(self):
        # TODO: Layani pelanggan terdepan
        pass

    # Menampilkan seluruh antrian
    def tampilkan(self):
        # TODO: Tampilkan seluruh antrian
        pass


# 3) Program utama
def main():
    q = QueueBengkel()  # Instansiasi queue bengkel

    # Perulangan menu utama sampai user pilih keluar
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")

        pilih = input("Pilih menu: ").strip()

        # Tambah pelanggan baru ke antrian
        if pilih == "1":
            no = input("No Antrian : ").strip()
            nama = input("Nama : ").strip()
            servis = input("Servis : ").strip()
            q.enqueue(no, nama, servis)

        # Layani pelanggan paling depan
        elif pilih == "2":
            q.dequeue()

        # Tampilkan seluruh antrian
        elif pilih == "3":
            q.tampilkan()

        # Keluar dari program
        elif pilih == "4":
            print("Program selesai. Terima kasih.")
            break

        # Input tidak valid
        else:
            print("Pilihan tidak valid")


# 4) Penanda eksekusi file utama

if __name__ == "__main__":
    main()