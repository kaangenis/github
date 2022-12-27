#Errors

#Errors ve Error handling uygulamanın çalıştırıldığı sırada ortaya çıkan problemlerin tanımlanması ve bu tanımlamaya bağlı olarak uygulamanın çalışmasını devam etmesini sağlama işlemine denir


#Bazı Error Türleri: 
#Error:
#print(a) => NameError => 'a' değişkeni tanımlanmadığı için makine NameError hatası verdi.
#int('1a2') => ValueError => int() fonksiyonu içerisine sadece sayıları aldığı için 'a' karakteri ValueError almamıza sebep oldu.
#print(10/0) => ZeroDivisionError => Herhangi bir sayıyı 0'a bölmeye çalıştığımız zaman alacağımız hata ZeroDivisionError'dur.
#print('denem'e) => SyntaxError => String bloğu içerisine (' ') kelimenin tamamını yerleştirmediğimiz için aldığımız hata SyntaxError'dur.

#Error Handling => Hata Yönetimi demektir.

#Detaylı bilgi 'docs.python.org' adresinde mevcut.(Builtin Exceptions)

x = int(input("X Değeri: "))
y = int(input("Y Değeri: "))

print("##################################################################")

try:
    print(x/y)
except ZeroDivisionError:
    print("Y değerini '0' girerseniz sonuç tanımsız olacaktır.")
#Yukarıdaki örnekte ZeroDivisionError üzerine bir Error Handling işlemi yapılmıştır.


print("##################################################################")


try:
    print(x/y)
except (ZeroDivisionError, ValueError):
    print("Geçersiz Değer Girdiniz.")
    
    
#Bu şekilde de çoklu ErrorHandling işlemleri yapılabilir.


print("##################################################################")


try:
    print(x/y)
except (ZeroDivisionError, ValueError) as E:
    print("Yanlış Değer Girdiniz. ")
    print(E)
    
#Bu şekilde hangi hata türünün 'except' bloğunu tetiklediğini bulabiliriz (as 'val' kullanarak.).


print("##################################################################")

try:
    print(x/y)
except:
    print("Yanlış Değer Girildi.")
    
    
#except bloğuna herhangi bir koşul tanımlanmasa bile çalışacaktır.


print("##################################################################")

try: 
    print(x/y)
except:
    print("Yanlış Değer Girdiniz.")
else:
    print("Değerlerde Problem Yok.")
    
    
#except bloğunun altına 'else' bloğu girilebilir bu sayede 'except' bloğu tetiklenmezse else bloğu da çalışacaktır.


print("##################################################################")

#Döngülerle bir örnek: 

while True:
    a = int(input("A değeri: "))
    b = int(input("B değeri: "))
    
    try:
        print(a/b)
    except:
        print("Girdiğiniz değerleri kontrol ediniz.")
    else:
        print("İşlem başarılı, uygulama kapatılıyor.")
        break
    
    
#Bu şekilde döngü içerisinde Hata Yönetimi yapılabilir.

