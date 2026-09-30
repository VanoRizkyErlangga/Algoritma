# Data awal: minimal 3 kontak (nama → nomor HP)
kontak = {
    "Budi": "081234567890",
    "Siti": "082345678901",
    "Andi": "083456789012"
}

# While loop untuk menu berulang
while True:
    print("\n===== BUKU KONTAK =====")
    print("1. Lihat semua kontak")
    print("2. Cari kontak by nama")
    print("3. Tambah kontak baru")
    print("4. Hapus kontak")
    print("5. Keluar")

    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        # Lihat semua kontak
        print("\n--- Daftar Kontak ---")
        if len(kontak) == 0:
            print("Kontak kosong.")
        else:
            for nama, nomor in kontak.items():
                print(f"  {nama} : {nomor}")

    elif pilihan == "2":
        # Cari kontak by nama menggunakan .get()
        nama_cari = input("Masukkan nama yang dicari: ")
        nomor = kontak.get(nama_cari)
        if nomor != None:
            print(f"Kontak ditemukan: {nama_cari} → {nomor}")
        else:
            print(f"Kontak '{nama_cari}' tidak ditemukan.")

    elif pilihan == "3":
        # Tambah kontak baru
        nama_baru = input("Masukkan nama: ")
        nomor_baru = input("Masukkan nomor HP: ")
        kontak[nama_baru] = nomor_baru
        print(f"Kontak '{nama_baru}' berhasil ditambahkan.")

    elif pilihan == "4":
        # Hapus kontak
        nama_hapus = input("Masukkan nama yang dihapus: ")
        if nama_hapus in kontak:
            del kontak[nama_hapus]
            print(f"Kontak '{nama_hapus}' berhasil dihapus.")
        else:
            print(f"Kontak '{nama_hapus}' tidak ditemukan.")

    elif pilihan == "5":
        # Keluar
        print("Terima kasih, program selesai.")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")