#====================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latiham Dasar 1A : Membaca seluruh isi File
#====================================================

#mMembuka file dengan read("r")

#Membuka file dalam satu string
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file=file.read() # membaca isi keseluruhan file dalam satu string
    print(isi_file)

    print("===Hasil Read===")
    print("Tipe Data:", type(isi_file))
    print("Jumlah Karakter", len(isi_file))
    print("Jumlah Baris", isi_file.count("\n")+1)

    #Membuka file perbaris
    print("===membaca File per baris===")
    jumlah_baris=0
    with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            jumlah_baris = jumlah_baris + 1
            baris = baris.strip() #Menghilangkan baris baru \n
            print("Baris ke-", jumlah_baris)
            print("Isinya :", baris)


#====================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : Parsing baris menjadi kolom data
#====================================================

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",") #Parsing data berdasarkan karakter
            print("NIM :", nim, "| Nama:", nama,"| Nilai: ", nilai)

#====================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca File dan Menyimpan ke List
#====================================================

data_list = [] # list untuk menampung data mahasiswa

with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()

            nim, nama, nilai = baris.split(",")
            #Simpan sebagai list " [nim,nama,nilai]"
            data_list.append([nim,nama,int(nilai)])

print("=== Data Mahasiswa dalam LIST===")
print (data_list)

print("=== Jumlah Record dalam LIST===")
print("Jumlah Record", len(data_list))

print("=== Menampilkan Data Record Tertentu ===")
print("Contoh Record Pertama: ", data_list[0]) #array dimulai dari 0

#====================================================
#Praktikum 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca File dan Menyimpan ke Dictionary
#====================================================

data_dict = {} #Buat variable untuk dictionary
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            nim, nama, nilai = baris.split(",")

            #Simpan data mahasiswa ke dictionary dengan key NIM 
            data_dict[nim] = {              #key
                 "nama": nama,              #values
                 "nilai" : int(nilai)       #values
            }
print("=== Data Mahasiswa dalam Dictionary===")
print(data_dict)