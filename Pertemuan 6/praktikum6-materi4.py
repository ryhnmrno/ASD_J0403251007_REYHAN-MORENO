#======================================================
# Nama : Reyhan Moreno
# NIM : J0403251007
# Kelas : B2
#======================================================

#======================================================
# Merge Sort dengan tracing
#======================================================

def merge_sort(data, depth=0):
    indent = " " * depth #indentasi berdasarkan level rekursi
    print(f"{indent}Merge_sort{data}")
    
    if len(data) <= 1: #Base case: jika data hanya memiliki 1 elemen atau kosong, sudah terurut
        return data
    
    #Divide : membagi data menjadi dua bagian
    mid = len(data) // 2 
    left = data[:mid] #slicing bagian kiri
    right = data[mid:] #slicing bagian kanan

    print(f"{indent} divide -> left = {left} | right = {right}")

    #recursive call
    left_sorted = merge_sort(left, depth + 1) #rekursif untuk bagian kiri
    right_sorted = merge_sort(right, depth + 1) #rekursif untuk bagian kanan

    merged = merge(left_sorted, right_sorted) #gabungkan hasil sorting bagian kiri dan kanan
    print(f"{indent} merge -> {left_sorted} + {right_sorted} = {merged}")
   
    return merged

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