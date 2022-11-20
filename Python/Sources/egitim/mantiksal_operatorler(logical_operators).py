
#detaylı anlatım proje kısmındaki logicaloperators.py'de mevcut.


#and
#mantık konusundaki "ve" bağlacı
#her iki degerin de doğru olması sonucu verecektir.
"""
x = 5 

deneme1 = x <10 and x>3 #True
print(deneme1)

#or
#mantık konusundaki "veya" bağlacı
#değerlerden herhangi birinin doğru olması sonucu verecektir.

deneme2 = (x > 0) or (x % 2 == 0) #True
deneme3 = (x < 0) or (x % 5 == 0) #True
deneme4 = (x < 0 ) or (x % 2 == 0) #False

print(deneme2)
print(deneme3)
print(deneme4)



#not
#olumsuzluk sağlar

y = 10

deneme5 = not(y > 5) #False
deneme6 = not(y < 5) #True

print(deneme5)
print(deneme6)

"""

grade = str(input("Harf Giriniz: "))
grade = grade.upper()


match grade:
    case "A":
        print("F Değeri Girdiniz.")
        
    case "B":
        print("B Değeri Girdiniz.")
        
    case "C":
        print("C Değeri Girdiniz.")
        
    case _:
        print("Uygun Olmayan Bir Değer Girdiniz.")
        
