import Modulmtk
import ModulTks
import database

def register():
    print("\n" + "="*35)
    print("      BUAT AKUN BARU (REGISTRASI)     ")
    print("="*35)
    
    username = input("Masukkan Username Baru : ").strip()
    password = input("Masukkan Password Baru : ").strip()

    if not username or not password:
        print("❌ Username dan password tidak boleh kosong!")
        return

    db = database.connect_db()
    if not db:
        print("❌ Gagal terhubung ke database.")
        return

    cursor = db.cursor()
    try:
        # Perintah SQL untuk memasukkan akun baru ke database
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        db.commit() # Menyimpan perubahan ke database MySQL
        print(f"\n✅ Akun '{username}' berhasil dibuat! Silakan login.")
    except Exception as e:
        print(f"\n❌ Gagal membuat akun: {e}")
    finally:
        db.close()

def login():
    print("\n" + "="*35)
    print("           HALAMAN LOGIN          ")
    print("="*35)
    
    username = input("Masukkan Username: ").strip()
    password = input("Masukkan Password: ").strip()

    db = database.connect_db()
    if not db:
        print("❌ Gagal terhubung ke database.")
        return False

    cursor = db.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    db.close()

    if user:
        print(f"\n✅ Login berhasil! Selamat datang, {username}.")
        return True
    else:
        print("\n❌ Username atau password salah!")
        return False

def main():
    # --- HALAMAN AWAL (LOGIN / REGISTRASI) ---
    while True:
        print("\n" + "="*35)
        print("      APLIKASI PYTHON MODULAR     ")
        print("="*35)
        print("1. Login")
        print("2. Buat Akun Baru (Registrasi)")
        print("3. Keluar")
        print("="*35)
        
        opsi = input("Pilih menu (1-3): ").strip()

        if opsi == "1":
            if login():
                break # Jika login sukses, keluar dari loop registrasi & masuk ke menu fitur
        elif opsi == "2":
            register() # Memanggil fungsi tambah user baru
        elif opsi == "3":
            print("\nTerima kasih! Program selesai. 👋")
            return
        else:
            print("❌ Pilihan tidak valid!")

    # --- MENU UTAMA FITUR APLIKASI ---
    while True:
        print("\n" + "="*35)
        print("         PILIH MENU UTAMA        ")
        print("="*35)
        print("1. Cek Bilangan Ganjil / Genap")
        print("2. Cek Bilangan Prima")
        print("3. Convert Format Teks")
        print("4. Hitung Kata & Karakter Teks")
        print("5. Keluar")
        print("="*35)
        
        pilihan = input("Pilih menu (1-5): ").strip()

        # --- MENU 1: GANJIL / GENAP ---
        if pilihan == "1":
            while True:
                print("\n--- MENU 1: GANJIL / GENAP ---")
                inp = input("Masukkan angka (ketik '~' untuk kembali ke menu): ").strip()
                if inp == '~':
                    break
                try:
                    angka = int(inp)
                    if hasattr(Modulmtk, 'ganjil_genap'):
                        print("Hasil:", Modulmtk.ganjil_genap(angka))
                    else:
                        print(f"Hasil: {angka} adalah {'Genap' if angka % 2 == 0 else 'Ganjil'}")
                except ValueError:
                    print("❌ Masukkan angka bulat yang valid!")

        # --- MENU 2: BILANGAN PRIMA ---
        elif pilihan == "2":
            while True:
                print("\n--- MENU 2: BILANGAN PRIMA ---")
                inp = input("Masukkan angka (ketik '~' untuk kembali ke menu): ").strip()
                if inp == '~':
                    break
                try:
                    angka = int(inp)
                    if hasattr(Modulmtk, 'cek_prima'):
                        print("Hasil:", Modulmtk.cek_prima(angka))
                    else:
                        print("❌ Fungsi 'cek_prima' belum ada di Modulmtk.py")
                except ValueError:
                    print("❌ Masukkan angka bulat yang valid!")

        # --- MENU 3: CONVERT FORMAT TEKS ---
        elif pilihan == "3":
            while True:
                print("\n--- MENU 3: CONVERT FORMAT TEKS ---")
                teks = input("Masukkan teks (ketik '~' untuk kembali ke menu): ").strip()
                if teks == '~':
                    break
                
                hasil = ModulTks.text_converter(teks)
                if hasil:
                    print("\n--- Hasil Konversi ---")
                    print("UPPERCASE   :", hasil["uppercase"])
                    print("lowercase   :", hasil["lowercase"])
                    print("Title Case  :", hasil["titlecase"])
                else:
                    print("❌ Teks tidak boleh kosong!")

        # --- MENU 4: HITUNG KATA & KARAKTER ---
        elif pilihan == "4":
            while True:
                print("\n--- MENU 4: HITUNG KATA & KARAKTER ---")
                teks = input("Masukkan teks (ketik '~' untuk kembali ke menu): ").strip()
                if teks == '~':
                    break
                
                hasil = ModulTks.count_words(teks)
                if hasil:
                    print("\n--- Hasil Hitungan ---")
                    print("Jumlah Kata     :", hasil["words"])
                    print("Jumlah Karakter :", hasil["chars"])
                else:
                    print("❌ Teks tidak boleh kosong!")

        # --- MENU 5: KELUAR ---
        elif pilihan == "5":
            print("\nTerima kasih! Program selesai. 👋")
            break

        else:
            print("❌ Pilihan tidak valid! Silakan pilih angka 1 - 5.")

if __name__ == "__main__":
    main()