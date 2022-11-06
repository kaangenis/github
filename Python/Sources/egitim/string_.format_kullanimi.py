#print deneme metodları
#print komutu içinde string formatının ardına ".format ve {} kullanımı ile kolayca str,int,float ve inputları ekleyebiliriz."



str_Deneme = "Deneme"
int_Deneme = 30
float_Deneme = 5.2
input_Deneme = input("Değer Giriniz: ")



print("Eğer Çalışırsa Burada {} ".format(str_Deneme),"yazacak.")
print("Eğer Çalışırsa Burada {} ".format(int_Deneme),"yazacak.")
print("Eğer Çalışırsa Burada {} ".format(float_Deneme),"yazacak.")
print("Eğer Çalışırsa Burada {} ".format(input_Deneme),"yazacak.")

input_Name = input("İsim: ")
input_Surname = input("Soyisim: ")
input_Age = input("Yaş: ")
#after = "ve ben"
#after2 = "yaşındayım."

#print("Merhaba Benim Adım {} {} {} {} {}".format(input_Name, input_Surname, after, input_Age, after2))

#print("Merhaba benim adım {} {} ve ben {} yaşındayım.".format(input_Name, input_Surname, input_Age))

print(f"Merhaba benim adım {input_Name} {input_Surname} ve ben {input_Age} yaşındayım.")