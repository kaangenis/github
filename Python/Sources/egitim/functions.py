"""

def deneme():
    print("Hello")

deneme()
deneme()
deneme()

"""


"""
isim = input("İsim: ")

def deneme2(name = "user"):
    print("Merhaba", name)

deneme2(isim)
deneme2()

"""

"""

def deneme3(name = "user"):
    return ("Hoşgeldin ", name)

msg = deneme3(isim)

print(msg)


num1 = int(input("Birinci Sayı: "))
num2 = int(input("İkinci Sayı: "))


def total(num1, num2):
    return num1 + num2 

result = total(num1 , num2)

print(result)

"""

name1 = str(input("İsim: "))
dg = int(input("Doğum Yılınız: "))

def yasHesapla(dogumYili):
    return 2022 - dogumYili

result1 = yasHesapla(dg)

print(result1)



def emeklilikHesapla(dogumYili, name1):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik < 0:
        print("Zaten Emeklisiniz.")
    elif emeklilik > 0:
        print(emeklilik, "Yıl Sonra Emekli Olacaksınız.")
    
sonuc = emeklilikHesapla(dg, name1)

print(sonuc)