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


############################################################################################################
hasta_Bilgi = {}
def hastaEkle():
    global hasta_TC
    hasta_TC = input("TC Kimlik Numarası: ")
    global hasta_Isim
    hasta_Isim = input("İsim: ")
    global hasta_Soyisim
    hasta_Soyisim = input("Soyisim: ")
    global hasta_Poliklinik
    hasta_Poliklinik = input("Poliklinik: ")

    hasta_Bilgi[hasta_TC] = {

        'İsim': [hasta_Isim],
        'Soyisim': [hasta_Soyisim],
        'Poliklinik': [hasta_Poliklinik]

    }





def hastaTcSırala():
    input_Tckn = input("Hasta TCKN: ")
    print(hasta_Bilgi[input_Tckn])

def hastaIsimSırala():
    input_Name = str(input("Hasta İsmi: "))
    print(hasta_Bilgi.get('İsim'))

def hastaGoruntule():

    print(hasta_Bilgi)


############################################################################################################





uygulamaDevam = True
while uygulamaDevam == True:
    print("Hastane Uygulamasına Hoşgeldiniz, Yapmak İstediğiniz İşlemi Seçiniz: ")
    print("1) Hasta Verisi Ekle. ")
    print("2) Hasta Verisi Görüntüle. ")
    print("3) Uygulamayı Kapat.")
    print("4) Hasta TCKN'ye Göre Sırala. ")
    print("5) Hasta İsmine Göre Sırala. ")
    i3 = int(input("=> "))

    if i3 == 1:
        hastaEkle()

    elif i3 == 2:
        hastaGoruntule()

    elif i3 == 3:
        uygulamaDevam = False

    elif i3 == 4:
        hastaTcSırala()

    elif i3 == 5:
        hastaIsimSırala()

    else:
        print("Yanlış Bir Değer Girdiniz Lütfen Kontrol Edin.")
        continue








