"""
1) Aşağıdaki program parçası işletildiği zaman ekran çıktısı nasıl olur?
    int i,toplam = 0;
    for( i=5 ; i <= 100 ; i=i+5)
    {
                toplam = toplam + i ;
     }
    printf("toplam= %d" , toplam);
"""

"""
2) 3’den başlayıp 3’er 3’er 300’e (dahil) kadar artan sayıların toplamını bulan ve yazdıran program parçasını yazınız.
"""



#Çözüm 2):
"""
x = 3
while x<=300:
    print(x)
    x = x + 3
    
"""

"""
3) Pozitif tamsayıların faktöriyeli 1 ‘den kendisine kadar olan sayıların çarpımından oluşur.
Örneğin 6 sayısının faktöriyeli 1X2X3X4X5X6 = 720 ‘dir . Sewizde klavyeden girilen sayının faktöriyelini bulup yazdıran program parçasını yazınız.
"""



#Çözüm 3):
"""
ucuncuSoru_List = []
ucuncuSoru = int(input("Faktöriyelini Almak İstediğiniz Sayıyı Giriniz: "))
while ucuncuSoru >= 1:
    print("zort")
    ucuncuSoru = ucuncuSoru-1
print(ucuncuSoru_List)


"""

"""
4) Klavyeden girilen 3 farklı sayının toplamını ve ortalamasını bulan ve yazdıran programı yazınız.
"""


#Çözüm-4
"""
soru_Dort_1 = int(input(("Birinci Sayısı Giriniz: ")))
soru_Dort_2 = int(input(("İkinci Sayısı Giriniz: ")))
soru_Dort_3 = int(input(("Üçüncü Sayısı Giriniz: ")))

toplam = soru_Dort_1 + soru_Dort_2 + soru_Dort_3
ortalama = toplam/3

print("Toplam: ", toplam)
print("Ortalama: ", ortalama)

"""


"""
5) 10 kişilik bir sınıftaki öğrencilerin bir derse ait notlarını ve adsoyadlarını okuyarak , notu 50’nin altında olan öğrencileri listeleyen programı yazınız.
"""



#Çözüm-5
"""
ogrenciler = ("Ali Kara", "Ayşe Eroğlu", "Veli Demir", "Merve Özkaynak", "Mehmet Ak", "Seda Çiçek", "Mahmut Değer", "Zeynep Ekin", "Tuna Tavus", "Aysu Karaca")
notlar = (50, 60, 35, 75, 40, 25, 80, 90, 45, 65)

sonuc = zip(ogrenciler, notlar)

print("Tüm Öğrencilerin Notları: " ,tuple(sonuc))
print(ogrenciler[2], "\n", ogrenciler[4], "\n", ogrenciler[5], "\n", ogrenciler[8])
"""


"""
6) Bir kurumda çalışanların yaşlarını  okuyarak yaş  ortalamasını bulan Java program parçasını yazınız. (veri girişini sonlandırmak için yaşa 0 (sıfır) giriniz) 
"""
#Çözüm-6
"""
calisanYaslari = []
uygulamaDevam = True
while uygulamaDevam == True:
    calisan_Yasi = int(input("Çalışan Yaşı: "))
    if calisan_Yasi != 0:
        calisanYaslari.append(calisan_Yasi)
        toplam = 0
        for sayi in calisanYaslari:
            toplam = toplam + sayi


    else:
        print(toplam/len(calisanYaslari))
        uygulamaDevam = False
"""


"""
7) Kişinin doğum yılını okuyarak yaşını bulan ve yazdıran programı yazınız.
"""

#Çözüm-7

"""
dogumYili = int(input("Doğum Yılınızı Giriniz: "))
yas = 2022 - dogumYili
print(yas, "Yaşındasınız. ")
"""

"""
8) Fibonnacci dizisinin ilk 20 terimini yazdıran programı yazınız.
( 0  1  1  2  3  5  8  13  21 .   .  . . . …………….)
"""

#Çözüm - 8 GERİ DÖN
"""
fiboList = [1]
fiboNum = 1
for sayi in fiboList:
    if len(fiboList) != 20:
        fiboNum = fiboNum + (fiboNum-1)
        fiboNum = fiboNum + 1
        fiboList.append(fiboNum)
        print(fiboList)
    else:
        continue
        
"""


"""
9] Farklı 10 sayıyı okuyarak en büyük ve en küçük sayıyı bulan ve yazdıran programı yazınız.
"""

#Çözüm-9
"""
onuncu_Ornek = []
uygulamaDevam = True
while uygulamaDevam == True:
    if len(onuncu_Ornek) != 10:
        sayi = int(input("Sayı: "))
        onuncu_Ornek.append(sayi)

    else:
        print("En Küçük Değer: " ,min(onuncu_Ornek) , "En Büyük Değer",  max(onuncu_Ornek))
        uygulamaDevam = False
        
"""
"""
10) İstenilen kez adı soyadı okuyan programı yazınız.
"""
#Çözüm-10
"""
isim_Soyisim = str(input("İsim ve Soyisim: "))
adet_On = int(input("Kaç Defa Yazdırmak İstiyorsunuz: "))

x = 0
while x < adet_On:
    print(isim_Soyisim)
    x = x + 1
    
"""


"""
11) İki sayıyı okuyan ve büyük sayıyı küçük sayıya bölen ve yazdıran programı yazınız.
"""

#Çözüm-11
"""
list_11 = []

sayi_1 = int(input("Birinci Sayı: "))
sayi_2 = int(input("İkinci Sayı: "))

list_11.append(sayi_1)
list_11.append((sayi_2))

print(list_11)
istenilen = max(list_11) / min(list_11)
print(istenilen)
"""

"""
12) 100’den başlayıp 50’ye kadar 5’er 5’er azalan sayıları yazdıran programı yazınız.
"""
#Çözüm-12
"""
degisken_12 = 100

while degisken_12 >= 50:
    print(degisken_12)
    degisken_12 = degisken_12 - 5
"""

"""
13) Malın fiyatını ve KDV oranını okuyarak KDV dahil satış fiyatını yazdıran programı yazınız.
"""
#Çözüm-13
"""
kdv_Oran = 0.18
vergisiz_Fiyat = int(input("Ürün Fiyatı: "))
son_Fiyat = (vergisiz_Fiyat * kdv_Oran) + vergisiz_Fiyat

print("Vergisiz Fiyat:",vergisiz_Fiyat ,  "KDV Dahil Fiyat: ", son_Fiyat)
"""

"""
14) Malın etiket fiyatını ve indirim oranını okuyarak indirimli fiyatını yazan programı yazınız.
"""

#Çözüm-14

"""
etiket_Fiyat = float(input("Etiket Fiyatı: "))
indirim_Oranı = float(input("İndirim Oranı: "))

indirimli_Fiyat = etiket_Fiyat - (etiket_Fiyat * indirim_Oranı/100)

print("Etiket Fiyatı:", etiket_Fiyat, "İndirimli Fiyat:", indirimli_Fiyat )
"""

"""
15) Bir çalışanın aylık maaşını okuyarak yıllık ve günlük kazancını bulan programı yazdırınız.
"""

#Çözüm-15
"""
aylik_Maas = int(input("Aylık Kazancınız Nedir: "))

gunluk = aylik_Maas/30
yillik = aylik_Maas * 12

print("Aylik Maaşınız: ", aylik_Maas, "Günlük Maaşınız: ", gunluk, "Yıllık Maaşınız: ", yillik)
"""




