#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
## hem sağ hem de sol taraftan okunduğunda aynı olan sayılardır.

def palindrom_mu(sayi):
    sayi_str = str(sayi)
    ters_sayi_str = sayi_str[::-1]
    if sayi_str == ters_sayi_str:
        return True
    else:
        return False

sayi = input("Bir sayı giriniz: ")

if palindrom_mu(sayi):
    print(sayi, "bir palindromdur.")
else:
    print(sayi, "bir palindrom değildir.")
