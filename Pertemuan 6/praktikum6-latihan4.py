#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
#======================================================

#======================================================
# Latihan 4 . Memahami Kode Program (Merge Sort) 
#======================================================

from heapq import merge


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = data[:mid]
    right = data[mid:]

    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)

    return merge(left_sorted, right_sorted)

# 1. Apa yang dimaksud dengan base case?
#    Jawaban:
#    Base case adalah kondisi pemberhentian rekursi, yaitu ketika
#    panjang data kurang dari atau sama dengan 1, sehingga data dianggap
#    sudah terurut dan fungsi mengembalikan data tersebut tanpa pemrosesan lebih lanjut.

# 2. Mengapa fungsi memanggil dirinya sendiri?
#    Jawaban:
#    Fungsi memanggil dirinya sendiri (rekursi) untuk membagi data menjadi bagian
#    yang lebih kecil secara berulang sampai base case tercapai, sehingga
#    memudahkan proses pengurutan bagian kecil sebelum digabungkan kembali.

# 3. Apa tujuan fungsi merge()?
#    Jawaban:
#    Fungsi merge() bertugas menggabungkan dua list yang sudah terurut menjadi
#    satu list terurut secara keseluruhan, sehingga hasil akhir dari merge_sort
#    adalah list yang sudah terurut seluruhnya.