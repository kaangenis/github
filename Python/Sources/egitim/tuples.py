list_1 = [1, 2, 3, "dört"]
tuple_1 = (4, 5, "altı")
tuple_2 = 6, "yedi", 8


print(list_1)
print(tuple_1)
print(tuple_2)

print(list_1[2])
print(tuple_1[2])

list_1[2] = "iki"
print(list_1)

#tuple_1[2] = 6
#print(tuple_1)
#tuple ve list arasındaki temel fark birinin değiştirilebilir diğerinin değiştirilemez olmasıdır.

tuple_3 = ("deneme", 3, "deneme2") + tuple_1

print(tuple_3)