"""
Daire Alanı: πr²
Daire Çevresi: 2πr
r: 3.14
"""

print("Dairenin alanını hesaplamak için Yarıçap (r) değerini giriniz... ")

r_Yaricap = input("Yarıçap (r) değeri: ")

pi_Sayisi = 3.14

daire_Alan = float(r_Yaricap) * float(r_Yaricap) * float(pi_Sayisi)

print("Yarıçapı", r_Yaricap , "olan Dairenin Alanı:", daire_Alan)

devam_Komutu = input('Aynı Dairenin Çevresini Hesaplamak için "Enter" tuşuna basın...')

daire_Cevre = 2 * pi_Sayisi * float(r_Yaricap)

print("Yarıçapı", r_Yaricap , "olan Dairenin Çevresi", daire_Cevre)
