"""
l1 = []
d1 = {}

i1 = input("Tc: ")
i2 = input("İsim: ")
i3 = input("Soyisim: ")
i4 = input("Poliklinik: ")

d1[i1]= {

    'İsim: ' : i2,
    'Soyisim: ': i3,
    'Poliklinik: ': i4

}

print(d1)
print(d1)

"""

hasta_Bilgi = {}

###################################FONKSİYONLAR######################################
def hastaEkle():
    global hasta_TC
    hasta_TC = int(input("TC Kimlik Numarası: "))
    global hasta_Isim
    hasta_Isim = input("İsim: ")
    hasta_Isim = hasta_Isim.capitalize()
    global hasta_Soyisim
    hasta_Soyisim = input("Soyisim: ")
    hasta_Soyisim = hasta_Soyisim.upper()
    global hasta_Poliklinik
    hasta_Poliklinik = input("Poliklinik: ")
    hasta_Poliklinik = hasta_Poliklinik.capitalize()

    hasta_Bilgi[hasta_TC] = {

        'İsim': [hasta_Isim],
        'Soyisim': [hasta_Soyisim],
        'Poliklinik': [hasta_Poliklinik]

    }
def hastaTcSırala():
    input_Tckn = int(input("Hasta TCKN: "))
    print(hasta_Bilgi[input_Tckn])


def hastaGoruntule():
    for a in hasta_Bilgi.values():
        print(a)

def hastaSil():
    print("Lütfen Silmek İstediğiniz Hastanın TCKN Bilgisini Giriniz: ")
    sil_Tckn = int(input("TCKN: "))

    print(f"{hasta_Bilgi[sil_Tckn]}'\n'Hasta Verilerini Silmek İstediğinize Emin Misiniz? (Y/N):  ")
    onay = str(input(" => "))
    onay = onay.upper()

    if onay == "Y":
        del hasta_Bilgi[sil_Tckn]
        print(sil_Tckn, "Bilgili Hasta Kaydı Başarıyla Silindi. ")

    else:
        print("Ana Sayfaya Yönlendiriliyorsunuz.")


############################################################################################################



uygulamaDevam = True
while uygulamaDevam == True:
    print("Hastane Uygulamasına Hoşgeldiniz, Yapmak İstediğiniz İşlemi Seçiniz: ")
    print("1) Hasta Verisi Ekle. ")
    print("2) Bütün Hastaları Görüntüle. ")
    print("3) Hasta TCKN'ye Göre Sırala. ")
    print("4) Hasta Verisi Sil. ")
    print("5) Uygulamayı Kapat.")
    i3 = int(input("=> "))

    if i3 == 1:
        hastaEkle()

    elif i3 == 2:
        hastaGoruntule()

    elif i3 == 3:
        hastaTcSırala()

    elif i3 == 4:
        hastaSil()

    elif i3 == 5:
        uygulamaDevam = False

    else:
        print("Yanlış Bir Değer Girdiniz Lütfen Kontrol Edin.")
        continue








