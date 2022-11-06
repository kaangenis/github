list1 = [1, 2, 3, 4, 5]

for deneme in list1:
    print(deneme)

list2 = ["Kaan", "Yaren", "Zeyno", "Tuna", "Ramo"]

for deneme2 in list2:
    print(f"My Name Is {deneme2}")


#for döngüsü listeyle tam çalışırken stringlerde ayırma işlemi yapar.

str1 = "Kaan Genis"

for deneme3 in str1:
    print(deneme3)



#for döngüsü dict ile de çalışır.

dict1 = {"a":2,"b":3, "c":4}


for deneme4 in dict1:
    print(deneme4)

#bu şekilde sadece keyleri alırız.

for deneme5, deneme6 in dict1.items():
    print(deneme6)

#.items() komutu ile sadece value ya da hem key hem value değerlerini alabiliriz.

