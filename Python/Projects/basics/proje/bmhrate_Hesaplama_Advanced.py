"""

bazal metabolizma:
kadınlar için: Kadınlar için BMH hesaplama: 655 + (9,6 x kg olarak ağırlık) + (1,8 x cm olarak boy) - (4,7 x yaş)
erkekler için: Erkekler için BMH hesaplama: 66 + (13,7 x kg olarak ağırlık) + (5 x cm olarak boy) - (6,8 x yaş)

"""

print("Bazal Metabolizma ve İdeal Kilo Hesaplama Uygulamasına Hoşgeldiniz...")

print("Hesaplamaya Başlamam İçin Lütfen Hesaplama İçin Gerekli Bilgileri Giriniz...")

isim_Input = input("İsim: ")
isim_Input = isim_Input.title()

soyisim_Input = input("Soyisim: ")
soyisim_Input = soyisim_Input.upper()

kilo_Input = float(input("KG Cinsinden Ağırlığınız (kg): "))

boy_Input = int(input("CM cinsinden boyunuz (cm): "))

yas_Input = float(input("Yaşınız: "))

cinsiyet_Input = input("Cinsiyet: ")
cinsiyet_Input = cinsiyet_Input.upper()


if cinsiyet_Input == "ERKEK" or "BAY":
    erkek_Kg = 13.7 * kilo_Input

    erkek_Boy = 5 * boy_Input

    erkek_Yas = 6.8 * yas_Input

    erkek_BMH = int(66 + erkek_Kg + erkek_Boy - erkek_Yas)

    print(f"Sayın {isim_Input} {soyisim_Input}, Bazal Metabolizma Hızınız (BMH): {erkek_BMH} ")

    print(f"Günlük {erkek_BMH} Kaloriden Az Aldığınız Koşulda Kalori Açığı Oluşturarak Sağlıklı Şekilde Kilo Verebilirsiniz... ")

    tavsiye_1 = erkek_BMH * 0.18

    tavsiye_2 = int(erkek_BMH - tavsiye_1)

    print(f"Gün İçinde Almanız Tavsiye Edilen Kalori: {tavsiye_2}")


elif cinsiyet_Input == "KADIN" or "BAYAN" or "KIZ":
    kadin_Kg = 9.6 * kilo_Input

    kadin_Boy = 1.8 * boy_Input

    kadin_Yas = 4.7 * yas_Input

    kadin_BMH = int(655 + kadin_Kg + kadin_Boy - kadin_Yas)

    print(f"Sayın {isim_Input} {soyisim_Input}, Bazal Metabolizma Hızınız (BMH): {kadin_BMH} ")

    print(f"Günlük {kadin_BMH} Kaloriden Az Aldığınız Koşulda Kalori Açığı Oluşturarak Sağlıklı Şekilde Kilo Verebilirsiniz... ")

    tavsiye_1 = kadin_BMH * 0.18

    tavsiye_2 = int(kadin_BMH - tavsiye_1)

    print(f"Gün İçinde Almanız Tavsiye Edilen Kalori: {tavsiye_2}")
