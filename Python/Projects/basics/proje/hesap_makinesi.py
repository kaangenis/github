print("Kaan Geniş Hesap Makinesine Hoşgeldiniz.")
print("Lütfen Yapmak İstediğiniz İşlemi '+', '-', '*', '/' olarak seçiniz.")


islem = str(input("Yapmak İstediğiniz İşlemi Seçiniz: "))
islem_Upper =islem.upper()

def hesapMak(a, b):
    if islem_Upper == "+" or islem_Upper == "TOPLAMA":
        return a + b
    elif islem_Upper == "-" or islem_Upper == "ÇIKARTMA" or islem_Upper == "ÇIKARMA":
        return a - b
    elif islem_Upper == "*" or islem_Upper == "ÇARPMA":
        return a * b 
    elif islem_Upper == "/" or islem_Upper == "BÖLME":
        return a / b

sayi1 = int(input("İşlem Yapmak İstediğiniz İlk Sayıyı Giriniz: "))
sayi2 = int(input("İşlem Yapmak İstediğiniz İkinci Sayıyı Giriniz: "))


sonuc = hesapMak(sayi1, sayi2)

print(sonuc)

