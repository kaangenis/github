#Inheritance bir miras gibidir

#Örneğin bir Person() classımız olduğunu düşünelim

#Bu class bir kişinin bilgilerini tanımlayacak.(name,surname,number,mail,adress)

#Bu classın altında oluşan diğer classlar verileri ana class'tan miras alacak

#Örneğin Student(Person) bir öğrencinin bilgilerini içerecekken.

#Teacher(Person) bir öğretmenin bilgilerini içerecek.

#Fakat bu iki alt class da verilerini ana class olan Person'dan alacak.

#Uygulama:

"""

class Person():
    def __init__(self, name, surname, age, adress, snumber = " ", trate= " "):
        self.name = name
        self.surname = surname
        self.age = age
        self.adress = adress
        self.snumber = snumber
        self.trate = trate
    

personStudent = Person("Kaan", "Geniş", 20, "Ankara", 20240326)
personTeacher = Person("Hasan", "Yılmazişler", 40, "Adana", trate= "90/100")


print(personStudent.adress, personStudent.snumber, personTeacher.trate)


"""

#Buraya kadar olan bölüm normal bir class tanımlamasıyla alakalıydı.
#Şimdi bunu Inheritance ile yapacağız.

"""

class Person():
    def __init__(self):
        print("Person Created")

class Student(Person):
    pass

p1 = Person()
s1  = Student()

#Görüldüğü üzere iki değişkenin çalışması sonucunda da "Person Created" çıktısı geldi.

"""

####


"""

class Person():
    def __init__(self):
        print("Person Created")

class Student(Person):
    def __init__(self):
        print("Student Created")

s1  = Student()

"""

#Eğer yukardaki gibi uygularsam Student classındaki "Student Created" çıktısı "Person Created" çıktısını yiyecektir.
#Bu yüzden aşağıdaki gibi yapacağız.

"""

class Person():
    def __init__(self):
        print("Person Created")

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("Student Created")

s1  = Student()

"""

#Böyle yaptığımız takdirde inheritance gerçekleşecektir ve iki Class iç içe şekilde çalışacaktır.

#Uygulanması:

"""

class Person():
    def __init__(self, fname, fsurname, adress, number):
        self.isim = fname
        self.soyisim = fsurname
        self.adres = adress
        self.number = number
        print("Person Created")

    def who_am_i(self):
        print("I am a Person.")
    
    def eat(self):
        print("I'm Eating Apple")



class Student(Person):
    def __init__(self, fname, fsurname, adress, number):
        Person.__init__(self, fname, fsurname, adress, number )
        print("Student Created")


p1 = Person("Hasan", "Yılmazişler", "Ankara", "Öğretmen")
s1  = Student("Kaan", "Geniş", "Ankara", 20240326)
print(s1.adres)
print(p1.number)


#Person classına eklediğimiz bütün fonksiyonlar aynı zamanda Student class'ını da ekleyecek aşağıda gözüktüğü gibi.

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()

"""

#Override:
#Override yukarıda yaptığımız işlemin tam tersini yapar, yani "who_am_i" metodu Student üzerinden çalıştığı zaman;
#"I am a Person." çıktısı yerine "I am a Student." çıktısını alırız.

"""

class Person():
    def __init__(self, fname, fsurname, adress, number):
        self.isim = fname
        self.soyisim = fsurname
        self.adres = adress
        self.number = number
        print("Person Created")

    def who_am_i(self):
        print("I am a Person.")
    
    def eat(self):
        print("I'm Eating Apple.")



class Student(Person):
    def __init__(self, fname, fsurname, adress, number):
        Person.__init__(self, fname, fsurname, adress, number )
        print("Student Created.")
    
    def who_am_i(self):
        print("I am a Student.")


p1 = Person("Hasan", "Yılmazişler", "Ankara", "Öğretmen")
s1  = Student("Kaan", "Geniş", "Ankara", 20240326)

p1.who_am_i()
s1.who_am_i()

"""

#Override yukardaki örnekteki gibi yapılır

#En önemli Inheritance özelliği şimdi başlıyor;
#Ana class içerisinden verileri kişiselleştirme.

class Person():
    def __init__(self, fname, fsurname, adress, number):
        self.isim = fname
        self.soyisim = fsurname
        self.adres = adress
        self.number = number
        print("Person Created")

    def who_am_i(self):
        print("I am a Person.")
    
    def eat(self):
        print("I'm Eating Apple.")



class Student(Person):
    def __init__(self, fname, fsurname, adress, number, snumber):
        Person.__init__(self, fname, fsurname, adress, number)
        self.snumber = snumber
        print("Student Created.")
    
    def who_am_i(self):
        print("I am a Student.")



class Teacher(Person):
    def __init__(self, fname, fsurname, adress, number, trate):
        Person.__init__(self, fname, fsurname, adress, number)
        self.trate = trate
        print("Teacher Created.")

    def who_am_i(self):
        print("I am a Teacher.")
    

#İşleri daha da kolaylaştıran metodlardan birisi de "Super()" metodudur.
#Bu metodu kullandığımız zaman self parametresini kullanmamıza gerek kalmaz.

class Manager(Person):
    def __init__(self, fname, fsurname, adress, number, role):
        super().__init__(fname, fsurname, adress, number)
        self.role = role
        print("Manager Created.")

    def who_am_i(self):
        print("I am a Manager")


s1  = Student("Kaan", "Geniş", "Ankara", 20240326, "80/100")
t1 = Teacher("Hasan", "Yılmazişler", "Adana", 5421234567, "90/100")
m1 = Manager("Mustafa", "Geniş", "Eskişehir", 5323227676, "Selling and Management")

s1.who_am_i()
t1.who_am_i()
m1.who_am_i()

print(s1.snumber)
print(t1.trate)
print(m1.role)
