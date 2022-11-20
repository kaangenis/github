l1 = []
l2 = []
l3 = []



def goruntule():
    print("Görüntülemek İstediğiniz Hastanın Baş Harfini Giriniz: ")
    print(l3)
    i5 = str(input(" => "))
    i5 = i5.upper()



def hastaekle():
    i1 = str(input("İsim Soyisim: "))
    i1 = i1.upper()
    i2 = str(input("Poliklinik: "))

    l1.append(i1)
    l1.sort()

    l2.append(i2)

    l3.append(i1[0])

def hastasil():
    i4 = int(input("Silmek İstediğiniz Hastanın Sıra Numarasını Giriniz: "))




uygulamaDevam = True
while uygulamaDevam == True:
    print("Hoşgeldiniz, Yapmak İstediğiniz İşlemi Seçiniz: ")
    print("1) Hasta Verisi Ekle. ")
    print("2) Hasta Verisi Görüntüle. ")
    print("3) Uygulamayı Kapat.")
    i3 = int(input("=> "))

    if i3 == 1:
        hastaekle()

    elif i3 == 2:
        goruntule()

    elif i3 == 3:
        uygulamaDevam = False

    else:
        print("Yanlış Bir Değer Girdiniz Lütfen Kontrol Edin.")
        continue






