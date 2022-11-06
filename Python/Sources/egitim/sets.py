#setler fonksiyon gibidir
#her elemandan bir tane mevcuttur
#indexlenemez
#.add ve .update komutlarıyla uyumludur


set_1 = {"apple", "banana", "orange"}

print(set_1)

set_1.add("mango")

print(set_1)

set_1.update(["strawberry", "grape"])

print(set_1)


#her elemandan bir tane mevcuttur

set_1.add("apple")

print(set_1)


#.remove komutu çalışır


deneme_Input = input("Silmek istediğiniz meyvenin adını giriniz: ")


set_1.remove(deneme_Input)

#.discard metodu da çalışır.



my_List1 = [1,2,2,3,4,5,6,7,9,0,0]


print(set_1)

print(set(my_List1))

print(my_List1)


#^^^^^^^^^^
#list ve set arasındaki temel fark.

