#====================================================================
#Nama : Reyhan Moreno
#NIM : J0403251007
#Kelas : TPL B2 
#====================================================================

#====================================================================
#Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar)
# input 3
# Masuk 1 -2 - 3
# Keluar 3 - 2 - 1
#====================================================================

def hitung(n):                    # Membuat fungsi hitung dengan konsep rekursi
    # Base case
    if n == 0:                    # Jika nilai n sudah 0
        print("Selesai")          # Menampilkan pesan bahwa proses telah selesai
        return                   # Menghentikan pemanggilan fungsi

    print("Masuk: ", n)           # Menampilkan nilai n saat fungsi mulai dijalankan
    hitung(n - 1)                 # Memanggil fungsi secara rekursif dengan nilai n dikurangi 1
    print("Keluar: ", n)          # Menampilkan nilai n setelah proses rekursi selesai

print("===Program Tracking===")   # Menmapilkan judul program
hitung(3)                         # Menjalankan fungsi hitung dengan nilai awal 3