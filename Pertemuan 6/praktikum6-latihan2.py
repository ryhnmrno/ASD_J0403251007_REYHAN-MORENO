#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
#======================================================

#======================================================
# Latihan 2 . Melengkapi Potongan Kode
#======================================================

# 1. Lengkapi kondisi agar menjadi sorting ascending.
#    Jawaban:

def insertion_sort_ascending(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] > key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data


# 2. Ubah agar menjadi descending.
#    Jawaban:

def insertion_sort_descending(data): 
    for i in range(1, len(data)): 
        key = data[i] 
        j = i - 1 
         
        while j >= 0 and data[j] < key: 
            data[j + 1] = data[j] 
            j -= 1 
         
        data[j + 1] = key 
     
    return data

# 1. Lengkapi kondisi agar menjadi sorting ascending.
#    Jawaban:
#    while j >= 0 and data[j] > key:
#    data[j + 1] = key


# 2. Ubah agar menjadi descending.
#    Jawaban:
#    while j >= 0 and data[j] < key:
#    data[j + 1] = key