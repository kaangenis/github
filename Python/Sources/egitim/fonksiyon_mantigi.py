
sehirler = ["Ankara", "Adana", "İzmir"]

sehir = str(input("Şehir İsmi: "))

"""

def change(n):
    n[0] = sehir
    sehirler.append(sehir)


print(sehirler)

change(sehirler)

print(sehirler)

"""

islem = input("Yapmak İstediğiniz İşlem Değiştirme mi Yoksa Ekleme mi Olacak: ")


if islem == "ekleme":
    def change(n):
        n.append(sehir)

elif islem == "degistirme":
    def change(n):
        n[0] = sehir


change(sehirler)
print(sehirler)