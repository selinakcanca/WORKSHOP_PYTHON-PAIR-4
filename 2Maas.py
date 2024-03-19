#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.

#birinci çözüm
def zamli_maas_hesapla(maas, zam_orani):
    zam_miktari = maas * (zam_orani / 100)
    zamli_maas = maas + zam_miktari
    return zamli_maas

maas = float(input("Maaşı giriniz: "))
zam_orani = float(input("Zam oranını giriniz (% olarak): "))

zamli_maas = zamli_maas_hesapla(maas, zam_orani)
print("Zamlı maaş:", zamli_maas)



#ikinci çözüm
yeniMaas=0
maas=input("Maaşı Gir : ")
zam=input("Zam Oranı(%) : ")
yeniMaas=float(maas)+(float(maas)*float(zam)/100)
print("Zamlı Maaş :",yeniMaas)

