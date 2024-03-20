#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

agirlik = float(input("Lütfen kilonuzu kg cinsinden giriniz: "))
boy = float(input("Lütfen boyunuzu metre cinsinden giriniz: "))
vki = agirlik/(boy*boy)

totalText = f"Vücut kitle indeksiniz= {vki}'dir."
print(totalText)



