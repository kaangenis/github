x = 2
y = 5
z = 10

a, b, c = 7, 8, 9


print(x,y,z)
print(a,b,c)

x += 5 #x = x + 5
x -= 5
x *= 5
x /= 5
z %= 5
y //=5
x **=5

print(x,y,z)


#tuple'lar fonksiyon gibidir her elemanın karşılığında sonuç veren başka bir eleman olmalıdır.


tuple_1 = 100, 200, 300

print(tuple_1)
print(type(tuple_1))

a, b, c = tuple_1

print(tuple_1)

print(b)



tuple_2 = 300,500,600,700


#fazlalık elemanları tek bir değerde toplamak için fazlalık elemanın önüne * eklemek gerekli
#*m

k, l, *m = tuple_2

print(tuple_2)
print(m[1])