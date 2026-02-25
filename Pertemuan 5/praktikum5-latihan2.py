#====================================================================
#Nama : Reyhan Moreno
#NIM : J0403251007
#Kelas : TPL B2 
#====================================================================

#====================================================================
# Latihan 2: Tracing Rekursi
#====================================================================

def countdown(n):                 # Mendefinisikan fungsi countdown dengan parameter n
    if n == 0:                    # Base case: jika nilai n adalah 0
        print("Selesai")          # Menampilkan bahwa proses telah selesai
        return                    # Menghentikan pemanggilan fungsi agar tidak berulang

    print("Masuk:", n)            # Menampilkan nilai n saat fungsi mulai dijalankan
    countdown(n - 1)              # Memanggil fungsi secara rekursif dengan nilai n dikurangi 1
    print("Keluar:", n)           # Menampilkan nilai n setelah proses rekursi selesai

countdown(3)                      # Memanggil fungsi countdown dengan nilai awal 3