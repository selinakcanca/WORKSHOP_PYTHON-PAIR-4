#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.

agirlik = float(input("Lütfen ağırlığınızı giriniz."))
boy = float(input("Lütfen boyunuzu giriniz."))
vki = agirlik / (boy*boy) #formülümüz

if 0 <= vki <= 18:
 print("Zayıfsınız")  
elif 18 < vki <=24:
 print("Normalsiniz")
elif 24 < vki <=29:
 print("Fazla kilolusunuz")
else:
 print("Vücut kitle indeksiniz çok yüksek, ,ideal kilonun çok üstündesiniz")



