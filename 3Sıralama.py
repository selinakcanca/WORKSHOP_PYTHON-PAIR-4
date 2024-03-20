#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.


sayi1 = int(input("Bir sayı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))
sayi3 = int(input("Üçüncü sayıyı giriniz: "))

if (sayi1>sayi2) and (sayi1>= sayi3):
    buyukSayi = sayi1
elif (sayi2>=sayi1) and (sayi2>=sayi3):
    buyukSayi=sayi2
else:
    buyukSayi=sayi3

totalText = f"Girdiğiniz sayılardan en büyüğü= {buyukSayi}."
print(totalText)
