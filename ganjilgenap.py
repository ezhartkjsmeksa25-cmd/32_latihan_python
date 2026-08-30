def cek_ganjil_genap():
    print("\n--- MENU GANJIL GENAP ---")
    while True:
        input_user = input("Masukkan angka (atau 'x' untuk kembali ke menu utama): ")
        if input_user.lower() == 'x':
            break
        
        try:
            angka = int(input_user)
            if angka % 2 == 0:
                print(f"{angka} adalah Bilangan Genap\n")
            else:
                print(f"{angka} adalah Bilangan Ganjil\n")
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.\n")

def cek_prima():
    print("\n--- MENU BILANGAN PRIMA ---")
    while True:
        input_user = input("Masukkan angka (atau 'x' untuk kembali ke menu utama): ")
        if input_user.lower() == 'x':
            break
            
        try:
            angka = int(input_user)
            if angka <= 1:
                print(f"{angka} Bukan Bilangan Prima\n")
            else:
                is_prima = True
                for i in range(2, int(angka**0.5) + 1):
                    if angka % i == 0:
                        is_prima = False
                        break
                
                if is_prima:
                    print(f"{angka} adalah Bilangan Prima\n")
                else:
                    print(f"{angka} Bukan Bilangan Prima\n")
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.\n")

# Navigasi Menu Utama
while True:
    print("=" * 30)
    print("        MENU UTAMA        ")
    print("=" * 30)
    print("1. Cek Bilangan Ganjil/Genap")
    print("2. Cek Bilangan Prima")
    print("3. Exit / Keluar")
    print("=" * 30)
    
    pilihan = input("Pilih menu (1/2/3): ")
    
    if pilihan == '1':
        cek_ganjil_genap()
    elif pilihan == '2':
        cek_prima()
    elif pilihan == '3':
        print("\nTerima kasih! Program selesai.")
        break
    else:
        print("\nPilihan tidak valid. Silakan pilih 1, 2, atau 3.\n")