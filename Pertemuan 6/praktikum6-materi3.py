#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
#======================================================

#======================================================
# Merge Sort : Ascending
#======================================================

def merge_sort(data):
    
    if len(data) <= 1: #Base case: jika data hanya memiliki 1 elemen atau kosong, sudah terurut
        return data
    
    #Divide : membagi data menjadi dua bagian
    mid = len(data) // 2 
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    #recursive call
    left_sorted = merge_sort(left) #rekursif untuk bagian kiri
    right_sorted = merge_sort(right) #rekursif untuk bagian kanan

    return merge(left_sorted, right_sorted) #gabungkan hasil sorting bagian kiri dan kanan

def merge(left,right):

    result = []
    i=0
    j=0

    #Membandingkan elemen kiri dan kanan
    while i < len(left) and j < len(right):
        if left [i] < right[j]: 
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1
    #Menambahkan sisa elemen jika ada
    result.extend(left[i:])
    result.extend(right[j:])

    return result

angka = [13,7,28,5,19,36,4]
print("Hasil Sorting:", merge_sort(angka))