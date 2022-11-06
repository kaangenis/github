
username = input("username: ")
password = input("password: ")

check = (username == "kaangenis") and (password == "12345678")

if check:
    print("Sisteme Giriş Başarılı.")
    print("Hoşgeldiniz...")
else:
    print("Lütfen Bilgilerinizi Kontrol Ediniz.")



x = input("X Değeri: ")
y = input("Y Değeri: ")

if x > y:
    print("X değeri Y değerinden büyük.")
elif x == y:
    print("X değeri Y değerine eşit")
elif y > x:
    print("X değeri Y değerinden küçük")
