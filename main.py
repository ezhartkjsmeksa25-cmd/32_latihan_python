# Program Cek Ganjil / Genap

while True:
    print("\n--- Program Cek Ganjil Genap ---")
    user_input = input("Masukkan angka (atau ketik 'keluar' untuk berhenti): ")

    # Kondisi untuk keluar dari program
    if user_input.lower() == 'keluar':
        print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
        break  # Menghentikan perulangan secara paksa

    try:
        # Mengubah input menjadi angka bulat
        angka = int(user_input)

        # Mengecek kondisi ganjil/genap
        if angka % 2 == 0:
            print(f"Angka {angka} adalah bilangan GENAP.")
        else:
            print(f"Angka {angka} adalah bilangan GANJIL.")

    except ValueError:
        print("Input tidak valid! Harap masukkan bilangan bulat atau ketik 'keluar'.")