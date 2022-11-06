name = "Kaan Genis"

for deneme in name:
    if deneme == "e":
        break
    print(deneme)


for deneme in name:
    if deneme == "e":
        continue
    print(deneme)


x = 0


#while x < 100:
#    x += 1
#    if x %2 == 1:
#        continue
#    print(x)


#while x < 100 :
#    x += 1
#    if x %2 == 1:
#        continue
#    elif x == 62:
#        break
#    print(x)


#1-100'e kadar olan tek sayıların toplamı:

x = 0
y = 0

while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    y = x + y
print(y)