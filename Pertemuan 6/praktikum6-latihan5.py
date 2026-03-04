#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
#======================================================

#======================================================
# Latihan 5 . Melengkapi Fungsi Merge 
#======================================================

# 1. Lengkapi kondisi agar menjadi ascending.
#    Jawaban:
#    Kondisi if yang harus dilengkapi adalah:
#    left[i] <= right[j]

def merge(left, right): 
    result = [] 
    i = 0 
    j = 0 
     
    while i < len(left) and j < len(right): 
        if left[i] <= right[j]: 
            result.append(left[i]) 
            i += 1 
        else: 
            result.append(right[j]) 
            j += 1 
     
    result.extend(left[i:]) 
    result.extend(right[j:]) 
     
    return result 


# 2. Jelaskan fungsi result.extend().
#    Jawaban:
#    Fungsi result.extend() digunakan untuk menambahkan semua elemen 
#    dari list yang diberikan (left[i:] atau right[j:]) ke akhir list result. 
#    Ini berguna untuk memasukkan sisa elemen dari list yang belum sepenuhnya 
#    diproses ke dalam hasil penggabungan.