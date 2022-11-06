number_List = [1, 10, 22, 5, 6, 84, 3]
letter_List = ["a", "y", "b", "z", "yaren", "8", "kaan"]



print(number_List)
print(letter_List)
print(min(number_List))
print(max(letter_List))


number_List.clear()
letter_List.clear()


number_Input = number_List.append(input("Sayı Giriniz: "))
letter_Input = letter_List.append(input("Harf ya da Kelime Giriniz: "))


print(number_List)
print(letter_List)


deneme = number_List

print(deneme)
print(f"{deneme}")