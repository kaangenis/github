l1 = []
l2 = []
l3 = []

x = 0
adetInput = int(input("Kac adet sayi girilecek: "))

while x < adetInput:
    firstInput = input(str("Sayi Giriniz: "))
    l1.append(firstInput)
    x += 1

while l1 != []:
    sonuc = int(l1[0]) ** len(l1[0])
    l2.append(sonuc)
    l3.append(l1[0])
    l1.pop(0)


print("Girdiğiniz Değerler: ",l3)
print("Girdiğiniz Değerlerin Basamaklarına Göre Üs Sonuçları: " ,l2)









