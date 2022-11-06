print("Vücut Kitle Endeksi (Sağlıklı Kilo Aralığı) Hesaplama Uygulamasına Hoşgeldiniz...")


#BMI = kg/cm^2

#gender = input("Cinsiyet: ")

name = input("İsim: ")
name = name.title()

surname = input("Soyisim: ")
surname = surname.upper()

age = input("Yaş: ")

height = int(input("Boy (CM): "))

weight = input("Kilo (KG): ")

cm_Kare = height * height

bmi = int(weight) / int(cm_Kare)

print(cm_Kare)