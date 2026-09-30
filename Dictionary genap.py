buku_kontak = {
    "Budi": "081234567890",
    "Andi": "089876543210",
    "Siti": "085612345678"
}
while True:
  
    print("\n=== MENU BUKU KONTAK ===")
    print("1. Lihat semua kontak")
    print("2. Cari kontak by nama")
    print("3. Tambah kontak baru")
    print("4. Hapus kontak")
    print("5. Keluar")
    
    pilihan = input("Pilih menu (1-5): ")
    
    if pilihan == "1":
        print("\n--- DAFTAR KONTAK ---")
        if not buku_kontak:
            print("Buku kontak masih kosong.")
        else:
            for nama, nomor in buku_kontak.items():
                print(f"- {nama}: {nomor}")
                
    elif pilihan == "2":
        nama_cari = input("\nMasukkan nama kontak yang dicari: ")
        hasil = buku_kontak.get(nama_cari)
        
        if hasil:
            print(f"Kontak ditemukan! {nama_cari}: {hasil}")
        else:
            print(f"Kontak dengan nama '{nama_cari}' tidak ditemukan.")
            
    elif pilihan == "3":
        nama_baru = input("\nMasukkan nama kontak baru: ")
        if nama_baru in buku_kontak:
            print("Nama tersebut sudah ada di kontak. Silakan gunakan nama lain atau hapus kontak lama terlebih dahulu.")
        else:
            nomor_baru = input("Masukkan nomor HP: ")
            buku_kontak[nama_baru] = nomor_baru
            print(f"Kontak {nama_baru} berhasil ditambahkan!")
            
    elif pilihan == "4":
        # Menu: Hapus kontak
        nama_hapus = input("\nMasukkan nama kontak yang ingin dihapus: ")
        # Mengecek apakah kontak ada menggunakan .get()
        if buku_kontak.get(nama_hapus):
            del buku_kontak[nama_hapus]
            print(f"Kontak {nama_hapus} berhasil dihapus.")
        else:
            print(f"Kontak dengan nama '{nama_hapus}' tidak ditemukan.")
            
    elif pilihan == "5":
        # Menu: Keluar
        print("\nTerima kasih telah menggunakan program buku kontak!")
        break
        
    else:
        print("\nPilihan tidak valid. Silakan pilih menu antara 1 sampai 5.")