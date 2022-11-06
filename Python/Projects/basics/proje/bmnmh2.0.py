print("Merhaba, Brüt Maaştan Net Maaş Hesaplama Uygulamasına Hoşgeldiniz...")


name_Input = input("İsim: ")
surname_Input = input("Soyisim: ")
name_Input = name_Input.title()
surname_Input = surname_Input.upper()


brut_Input = input("Brüt Maaşınızı Giriniz: ")


kdv = 0.30
vergi_Orani = float(brut_Input) * float(kdv)
net_Maas = int(brut_Input) - int(vergi_Orani)


print(f"Sayın {name_Input} {surname_Input} Net Maaşınız: {net_Maas} Türk Lirası.   ")