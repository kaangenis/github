#range




for deneme in range(10):
    print(deneme)

for deneme2 in range(5,20):
    print(deneme2)

for deneme3 in range(10,100,10):
    print(deneme3)



"""

#enumarete

string1 = "Hoşgeldiniz"

for sayi, harf in enumerate(string1):
    print(f"Sayi: {sayi}, Harf: {harf}   ")


"""

#zip

"""

list1 = [1,2,3,4,5]

list2 = ["a", "b", "c", "d", "e"]

list3 = [100,200,300,400,500]

print(list(zip(list1, list2)))

print(list(zip(list1, list2, list3)))

print(list(zip(list1, list3)))


for sayi, harf in zip(list1,list2):
    print(f"Sayısı: {sayi}, Harfi: {harf} ")

"""




input_Deneme = int(input("Başlangıç Sayısı: "))
input2 = int(input("Bitiş Sayısı: "))

for deneme9 in range(input_Deneme, input2, 10):
    print(deneme9)
