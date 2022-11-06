name = str(input("İsim: "))
surname = str(input("Soyisim: "))
birth = str(input("Doğum Tarihi: "))
hesapno = int(input("Hesap No: "))
parola = str(input("Parola: "))



class Finans():
    def __init__(self, isim, soyisim, birth, hesapno, parola):
        self.isim = isim
        self.soyisim = soyisim
        self.birth = birth
        self.hesapno = hesapno
        self.parola = parola



my_Finans = Finans(name, surname, birth, hesapno, parola)

