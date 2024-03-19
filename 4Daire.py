#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

pi = 3.14159
yaricap = int(input("Alan giriniz:"))

daireAlan = pi * yaricap * yaricap
daireCevre = 2 * pi * yaricap

print("Dairenin alanı:",daireAlan, '', "ve ","Dairenin çevresi:", daireCevre)