#while döngüsü liste yaratma mantığında çalışır.

#1-100 aralığında bir liste yaratmak istendiği zaman:

x = 1

while x <= 100:
    print(x)
    x = x + 1

print("bitti...")

#aynı zamanda if ile kullanılabilir.

y = 2

while y <= 200:
    if y %2 ==00:
        print(y)
    y = y + 1
print("Bitti...")

#ikisi birlikte de yazdırılabilir.

z = 1

while z <= 100:
    if z %2 == 0:
        print(f"Çift Sayı: {z}")
    else:
        print(f"Tek Sayı: {z}")
    z = z + 1

print("BİTTİ")



#input ve stringlerle çalışabilir.

name = "" #Şu anda bu string False değeri verir. Bu yüzden while döngüsünün yanına not operatörünü kullanıyoruz.

while not name.strip():
    name = input("İsminizi Giriniz: ")
print(f"Merhaba {name} ")