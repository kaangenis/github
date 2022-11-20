isim_Liste = []
soyisim_Liste = []
poliklinik_Liste = []

tum_Listeler = zip(isim_Liste, soyisim_Liste, poliklinik_Liste, strict=True)

def hastaEkle():
    isim_Input = str(input("Hasta İsmi: "))
    soyisim_Input = str(input("Hasta Soyismi: "))
    poliklinik_Input = str(input("Poliklinik: "))

    isim_Liste.append(isim_Input)
    soyisim_Liste.append(soyisim_Input)
    poliklinik_Liste.append(poliklinik_Input)

def hastaGoruntule():
    print(list(tum_Listeler))

def isimdenGoruntule():
    arama_Isim = input("Aramak İstediğiniz Hastanın Adını Giriniz: ")
    if arama_Isim in isim_Liste:
        print(list(tum_Listeler)[str(arama_Isim)])
        #INDEXXXXXXXXX
    else:
        print("Çalışmadı")





uygulamaDevam = 1
while uygulamaDevam == 1:
    print("Hastane Uygulamasına Hoşgeldiniz.")
    print("Lütfen Aşağıdaki Menüden Yapmak İstediğiniz İşlemi Seçiniz.")
    print("1) Yeni Hasta Kaydı Ekle ")
    print("2) Hasta Kayıtlarını Görüntüle ")
    print("3) Hasta İsmine Göre Görüntüle ")
    print("4) Programı Kapat ")

    menuSec = int(input(" => "))

    if menuSec == 1:
        hastaEkle()

    elif menuSec == 2:
        hastaGoruntule()

    elif menuSec == 3:
        isimdenGoruntule()

    elif menuSec == 4:
        uygulamaDevam = 0

    else:
        print("zort")


