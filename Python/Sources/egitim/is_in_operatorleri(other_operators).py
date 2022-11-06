#in

a = [1, 2, "üç", 5000, 70.8]

deneme = "üç" in  a

print(deneme)



#is

x = 5
y = 10
z = 5

deneme_1 = x is y
deneme_2 = x is z

print(deneme_1)
print(deneme_2)

#is operatoru valuelerde eşitlik verir ama her list farklı adrese sahip olduğu için listlere farklı davranır

k = ["a", "b", "c"]
m = ["a", "b", "c"]

deneme_3 = k is m

print(deneme_3)


#?örnek:
input_Deneme = input("İsim: ")

deneme_4 = input_Deneme is "Kaan"

print(deneme_4)

