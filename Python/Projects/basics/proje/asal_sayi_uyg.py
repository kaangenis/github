#Kullanıcıdan bir sayı isteyin ve bu sayının asal olup olmadığını kontrol edin

x = 0
while x < 5:
            sayi = int(input("Sayi Giriniz: "))
            zort = True
            for x in range(2, sayi):
                                    if (sayi % x == 0) and (sayi % sayi == 0) and (sayi % 1 ==0):
                                                                                                zort = False
                                                                                                break

if zort == False or sayi == 1:
    print("Sayı Asal Değildir.")
else:
    print("Sayı Asaldır.")

x = x + 1