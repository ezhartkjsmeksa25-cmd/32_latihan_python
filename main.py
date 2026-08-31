import Modulmtk
import ModulTks

def main():
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
                    print("UPPERCASE  :", hasil["uppercase"])
                    print("lowercase  :", hasil["lowercase"])
                    print("Title Case :", hasil["titlecase"])
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