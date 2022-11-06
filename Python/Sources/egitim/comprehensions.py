from tkinter import Y


numbers0 = []
for x in range(10):
    numbers0.append(x)
print(numbers0)


#yukarıyı tek satırda yapmamızı sağlayan şey comprehensions

input_a = int(input("Sayi Giriniz: "))

numbers2 = [x for x in range(input_a)]

print(numbers2)

numbers3 = [(x**2) for x in range(input_a) if x %2 ==0]

print(numbers3)


######################-comprehension-######################

my_String = "Hello"
my_List = [x for x in my_String]

print(my_List)




#En önemli kısım

years = [2020,2019,1970,1954,1918]

ages = [2022 - age for age in years ]

for age2 in ages:
    print(f"I'm {age2} years old.")


#Kolay bir şekilde Liste belirlemeleri yapılabilir.
#Örnek:

input_Yas = int(input("Doğum Tarihinizi Giriniz: "))

listdeneme = [input_Yas]

age_3 = [2022 - age4 for age4 in listdeneme]

for age5 in age_3:
    print(f"{age5} Yaşındasınız.")

##


input_b = int(input("B Sayısı: "))
numbers9 = [x**2 if x % 2 ==0 else "TEK" for x in range(input_b)]

print(numbers9)




##

deneme = [(x,y) for x in range(5) for y in range(5)]

for harf in deneme:
    print(harf)
