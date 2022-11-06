#classlar kendi komutlarımızı yaratma fırsatı sunar

"""

class Deneme():


    mail = "No Information"


    def __init__(self,name,surname,year,adress):
        self.name = name
        self.surname = surname
        self.year = year
        self.adress = adress


    def intro(self):
        print(f"Merhaba {p1.name} {p1.surname} ")


    def yasHesapla(self):
        yas = 2022 - p1.year
        print(f"Yaşınız {yas} ")



#aynısını return metodu ile de yapabiliriz:

    def yasHesapla(self):
        return 2022 - p1.year


#Fakat bunu yaptığımız zaman en son kodu çalıştıracağımız noktada print(f) komutu kullanmamız gerekiyor.




kullanici_Bilgi = Deneme("Kaan", "Geniş", "2001", "Ankara")

#ya da 

p1 = Deneme(name= "Yaren", surname= "Özkaya", year= 2001, adress= "Adana")
p2 = Deneme(name= "Kaan", surname= "Geniş", year= 2002, adress= "Ankara")

print(kullanici_Bilgi.adress)
print(kullanici_Bilgi.mail)
print(p1.adress)
print(p2.surname)
p1.intro()
p1.yasHesapla()

"""


#Classlar ile birçok işlem çok daha rahat yapılabilir Örn: Daire Hesaplaması:

class Circle():

    #Bu kısım class object attribute

    pi = 3.14

    def __init__(self, yaricap= 1):
        self.yaricap = yaricap

    #Bu kısım da Class'ın methodları.

    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap

    def alanHesapla(self):
        return self.pi * (self.yaricap ** 2)

c1 = Circle() #Bu durumda Yarıçap değeri tanımlı olarak 1 olacak
c2 = Circle(5)

print(c1.cevreHesapla())
print(c1.alanHesapla())

print(c2.cevreHesapla())
print(c2.alanHesapla())



#Class ve Class Methodları Kullanımı İçin Yukardaki Daire Örneği Kapsamlı Olarak Öğretici.
