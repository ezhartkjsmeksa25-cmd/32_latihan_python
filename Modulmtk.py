def ganjil_genap(angka):
    """Menentukan apakah bilangan ganjil atau genap"""
    if angka % 2 == 0:
        return f"{angka} adalah Bilangan GENAP"
    else:
        return f"{angka} adalah Bilangan GANJIL"


def cek_prima(angka):
    """Menentukan apakah bilangan prima atau bukan"""
    if angka <= 1:
        return f"{angka} Bukan Bilangan Prima"
    
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return f"{angka} Bukan Bilangan Prima"
            
    return f"{angka} Adalah BILANGAN PRIMA"