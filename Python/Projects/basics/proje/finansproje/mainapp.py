print("Finans Uygulamasına Hoşgeldiniz..")
print("Mevcut Üyelikle Devam Etmek İçin 1'i Seçin.")
print("Yeni Üyelik Oluşturmak İçin 2'yi Seçin. ")
i1 = int(input(("1-) Mevcut Üyelik ile Devam Etmek İstiyorum. ""\n2-) Yeni Üyelik Oluşturmak İstiyorum." "\n: ")))

if i1 == 2:
    import denemebase
else:
    pass

print(f"Hoşgeldiniz Sayın, {denemebase.my_Finans.isim} {denemebase.my_Finans.soyisim} ")





