daftar_siswa = []


def tentukan_kategori(nilai):
    """Menentukan kategori huruf berdasarkan nilai."""
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 60:
        return "C"
    elif nilai >= 50:
        return "D"
    else:
        return "E"
    
    
def tambah_data():
    print("\n--- TAMBAH DATA SISWA ---")
    nama = input("Masukkan nama siswa: ")
    
    # validasi input nilai agar berupa angka 0 - 100
    while True:
        try:
            nilai = float(input("Masukkan nilai (0-100): "))
            if 0 <= nilai <= 100:
                break
            print("Nilai harus antara 0 sampai 100!")
        except ValueError:
            print("Harap masukkan angka yang benar!")
            
    kategori = tentukan_kategori(nilai)
    
    # Simpan data ke dalam dictionary lalu masukkan ke list
    siswa = {"nama": nama, "nilai": nilai, "kategori": kategori}
    daftar_siswa.append(siswa)
    print(f"Data siswa '{nama}' berhasil ditambahkan!")
    
    
def tampilkan_data():
    print("\n--- DAFTAR SISWA ---")
    if len(daftar_siswa) == 0:
        print("Belum ada data siswa.")
        return
    
    # Tampilkan menggunakan perulangan biasa yang mudah dibaca
    for i , siswa in enumerate(daftar_siswa, 1):
        print(
            f"{i}, Nama: {siswa['nama']} | Nilai: {siswa['nilai']} | Kategori: {siswa['kategori']}"
        )
        
        
def hitung_rata_rata():
    print("\n--- RATA-RATA NILAI ---")
    if len(daftar_siswa) == 0:
        print("Belum ada data siswa.")
        return
    
    total = 0
    for siswa in daftar_siswa:
        total += siswa["nilai"]
        
    rata_rata = total / len(daftar_siswa)
    print(f"Jumlah siswa : {len(daftar_siswa)}")
    print(f"Rata-rata    : {rata_rata}")
    
    
def cari_nilai_tertinggi():
    print("\n--- NILAI TERTINGGI ---")
    if len(daftar_siswa) == 0:
        print("Belum ada data siswa.")
        return
    
    # Mencari nilai tertinggi menggunakan perulangan biasa (tanpa lambda)
    tertinggi = daftar_siswa[0]
    for siswa in daftar_siswa:
        if siswa["nilai"] > tertinggi["nilai"]:
            tertinggi = siswa
            
    print(f"Nama     : {tertinggi['nama']}")
    print(f"Nilai    : {tertinggi['nilai']}")
    print(f"Kategori : {tertinggi['kategori']}")
    
    
def main():
    while True:
        print("\n==========================")
        print(" PENGELOLAAN DATA SISWA ")
        print("==========================")
        print("1. Tambah Data")
        print("2. Tampilkan Data")
        print("3. Hitung Rata-rata")
        print("4. Cari Nilai Tertinggi")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            tambah_data()
        elif pilihan == "2":
            tampilkan_data()
        elif pilihan == "3":
            hitung_rata_rata()
        elif pilihan == "4":
            cari_nilai_tertinggi()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid, coba lagi.")
            
            
if __name__=="_main_":
    main()