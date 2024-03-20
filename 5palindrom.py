#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
## hem sağ hem de sol taraftan okunduğunda aynı olan sayılardır.

def palindrom_mu(sayi):
    sayi_str = str(sayi)
    tersi = sayi_str[::-1]

    if sayi_str == tersi:
        return True
    else:
        return False

sayi = (input("Bir sayi girin: "))

if palindrom_mu(sayi):
    print("Girdiğiniz sayi bir palindromdur.")
else:
    print("Girdiğiniz sayi bir palindrom değildir.")


""" 2.alternatif 


    sayi =input("Lütfen bir sayi giriniz: ")

tersten = sayi[::-1]

if sayi == tersten:
    print("Bu sayi bir palindromdur.")
else:
    print("Bu sayi bir palindrom değildir.")


"""
