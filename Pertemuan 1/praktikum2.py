#====================================================
#Praktikum 2 : Konsep ADT dan File Handling
#Latiham Dasar 1 : Membuat fungsi load data
#====================================================

#membuat fungsi membaca data mahasiswa
nama_file = "data_mahasiswa.txt"

def baca_data_mahasiswa(nama_file):
    data_dict = {} #inisialisasi data dictionary

    with open(nama_file, "r", encoding="utf-8") as file: # pakai parameter
        for baris in file:
            baris = baris.strip() #menghilang karakter baris baru

            if baris == "":  # menghindari baris kosong
                continue

            nim, nama, nilai = baris.split(",")

            data_dict[nim] = { #key
                "nama": nama,  #values
                "nilai": nilai #values
            }

    return data_dict

#memanggil fungsi baca_data_mahasiswa
#buka_data = baca_data_mahasiswa(nama_file)
#print("Jumlah data terbaca:", len(buka_data))

#====================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latiham Dasar 2 : Membuat menampilkan data
#====================================================

def tampilkan_data(data_dict):

    if len(data_dict) == 0:
        print("Data kosong")
        return    

    #membuat tabel Header
    print("\n=== Daftar Mahasiswa ===")
    print(f"{'NIM':10} | {'Nama':<12} | {'Nilai':>5}")
    print("-" * 32) #membuat garis header

    # Isi tabel
    for nim in sorted(data_dict.keys()):
        nama = data_dict[nim]["nama"]
        nilai = data_dict[nim]["nilai"]

        print(f"{nim:10} | {nama:<12} | {nilai:>5}")

#memanggil fungsi menampilkan data
#tampilkan_data(buka_data)

#====================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latiham Dasar 3 : Cari data
#====================================================

def cari_data(data_dict):

    nim_cari = input("Massukan NIM yang ingin dicari : ").strip()
     
    if nim_cari in data_dict:
        nama = data_dict[nim_cari]["nama"]
        nilai = data_dict[nim_cari]["nilai"]

        print("\n=== Data Mahasiswa Ditemukan===")
        print(f"NIM        : {nim_cari}")
        print(f"Nama       : {nama}")
        print(f"Nilai      : {nilai}")
    else:
        print("\nData Tidak Ditemukan")

 #   cari_data(buka_data)


#====================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latiham 4 : update data
#====================================================

def update_nilai(data_dict):
    #cari nim mahasiswa yang akan diupdate nilainya
    nim = input("Masukkan NIM mahasiswa yang akan diupdate nilainya: ").strip()

    if nim not in data_dict:
        print("NIM tidak Ditemukan, update dibatalkan")
        return

    try:
        nilai_baru = int(input("Masukkan nilai baru (0-100): ").strip())
    except ValueError:
        print("Nilai harus berupa angka. Update dibatalkan")
        return

    if nilai_baru < 0 or nilai_baru > 100:
        print("Nilai harus antara 0 sampai 100. Update dibatalkan")
        return

    nilai_lama = data_dict[nim]["nilai"]

    #memasukkan nilai update ke dictionary
    data_dict[nim]["nilai"] = nilai_baru

    print("Nilai berhasil diupdate")
    print("Nilai lama:", nilai_lama)
    print("Nilai baru:", nilai_baru)


#====================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latiham 5 :  Membuat Fungsi menyimpan perubahan data ke file
#====================================================

def simpan_data(nama_file, data_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for nim in sorted(data_dict.keys()):
            nama = data_dict[nim]["nama"]
            nilai = data_dict[nim]["nilai"]

            file.write(f"{nim},{nama},{nilai}\n")

    print("Data Berhasil Disimpan")


#====================================================
#Praktikum 2 : Konsep ADT dan File Handling (STUDI KASUS)
#Latiham 6 :  Membuat Fungsi menyimpan perubahan data ke file
#====================================================

def main():

    #menjalankan fungsi 1 load data
    buka_data = baca_data_mahasiswa(nama_file)

    while True:

        print("\n=== MENU DATA MAHASISWA===")
        print("1. Tampikan semua data")
        print("2. Cari data berdasarkan NIM")
        print("3. Update nilai mahasiswa")
        print("4. Simpan data ke file")
        print("0. Keluar")

        pilihan = input("Pilihan Menu : ").strip()

        if pilihan == "1":
            tampilkan_data(buka_data)

        elif pilihan == "2":
            cari_data(buka_data)

        elif pilihan == "3":
            update_nilai(buka_data)

        elif pilihan == "4":
            simpan_data(nama_file, buka_data)

        elif pilihan == "0":
            print("Program Selesai")
            break

        else:
            print("data tidak valid")


if __name__ == '__main__':
    main()
