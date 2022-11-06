"""
Daire Alanı: πr²
Daire Çevresi: 2πr
r: 3.14
"""

print("Daire alan ve çevre hesaplama.")

print("Dairenin alanını ve çevresini hesaplamak için Yarıçap (r) değerini giriniz... ")

r_Yaricap = float(input("Yarıçap (r) değeri: "))

pi_Sayisi = 3.14

daire_Alan = float(r_Yaricap**2) * float(pi_Sayisi)

daire_Cevre = 2 * pi_Sayisi * float(r_Yaricap)

print("Yarıçapı", r_Yaricap,  "olan Dairenin Alanı: ", daire_Alan, "\nYarıçapı", r_Yaricap, "olan Dairenin Çevresi: ", daire_Cevre)