def cek_ganjil_genap():
    print("\n--- MENU GANJIL GENAP ---")
    while True:
        input_user = input("Masukkan angka atau 'x' untuk stop): ")
        if input_user.lower() == 'x':
            print("Kembali ke program utama.")
            break
        
        try:
            angka = int(input_user)
            if angka % 2 == 0:
                print(f"{angka} adalah Bilangan Genap\n")
            else:
                print(f"{angka} adalah Bilangan Ganjil\n")
        except ValueError:
            print("Input tidak valid! Masukkan angka yang benar.\n")

cek_ganjil_genap()
def cek_prima():
    print("\n--- MENU BILANGAN PRIMA ---")
    while True:
        input_user = input("Masukkan angka (atau 'x' untuk stop): ")
        if input_user.lower() == 'x':
            print("Kembali ke program utama.")
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

cek_prima()