while True:
    angka = input("Masukkan bilangan (ketik angka berapa saja, atau x untuk stop): ")
    if angka == 'x':
        print("Terima kasih")
        break

    angka = int(angka)
    if angka % 2 == 0:
        print("Bilangan Genap")
    else:
        print("Bilangan Ganjil")