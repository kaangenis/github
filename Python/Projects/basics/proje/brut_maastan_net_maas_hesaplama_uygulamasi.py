#net maas hesaplama

vergi_Orani = 0.30

print("Hoşgeldiniz...")
print("Net Maaşınızı hesaplamak için lütfen isim soyisim ve brüt maaşınızı giriniz...")

isim_Soyisim = str(input("İsim Soyisim: "))
brut_Maas = int(input("Brüt Maaş: "))

vergi_Miktari = vergi_Orani * brut_Maas

net_Maas = int(brut_Maas - vergi_Miktari)

int_Net = str(net_Maas)

print("Sayın" + " "  + isim_Soyisim + " "  + "Net Maaşınız" + " " + int_Net + " " + "Türk Lirası")

input('Programdan Çıkmak İçin "Enter" Tuşuna Basınız...')