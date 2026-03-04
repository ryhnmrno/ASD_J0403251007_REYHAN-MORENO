#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
#======================================================

#======================================================
# Latihan 1 . Memahami Kode Program (Insertion Sort) 
#======================================================

def insertion_sort(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data 

# 1. Mengapa perulangan dimulai dari indeks 1?
#    Jawaban: Karena elemen pertama (indeks 0) dianggap sudah terurut,
#    sehingga perbandingan dimulai dari elemen kedua (indeks 1).

# 2. Apa fungsi variabel key?
#    Jawaban: Untuk menyimpan nilai elemen yang sedang diproses
#    dan akan disisipkan ke posisi yang tepat pada bagian yang sudah terurut.

# 3. Mengapa digunakan while, bukan for?
#    Jawaban: Karena jumlah pergeseran elemen tidak diketahui sebelumnya.
#    Perulangan berjalan selama elemen sebelumnya lebih besar dari key.

# 4. Operasi apa yang terjadi di dalam while?
#    Jawaban: Terjadi pergeseran elemen ke kanan (data[j] ke data[j+1])
#    untuk memberi ruang agar key dapat ditempatkan di posisi yang benar.