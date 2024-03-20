#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

maas = float(input("Lütfen maaşınızı giriniz: "))
zamOrani = float(input("Lütfen zam oranınızın yüzde kaç olduğunu giriniz: "))
zamliMaas = (maas*(100 + zamOrani)/100)

totalText = f"Zamlı maaşınız= {zamliMaas}"
print(totalText)

