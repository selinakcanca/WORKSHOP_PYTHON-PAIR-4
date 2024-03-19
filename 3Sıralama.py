#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.


def en_buyuk_bul(sayi1, sayi2, sayi3):
    if sayi1 >= sayi2 and sayi1 >= sayi3:
        return sayi1
    elif sayi2 >= sayi1 and sayi2 >= sayi3:
        return sayi2
    else:
        return sayi3

sayi1 = float(input("Birinci sayıyı giriniz: "))
sayi2 = float(input("İkinci sayıyı giriniz: "))
sayi3 = float(input("Üçüncü sayıyı giriniz: "))

en_buyuk = en_buyuk_bul(sayi1, sayi2, sayi3)
print("En büyük sayı:", en_buyuk)
