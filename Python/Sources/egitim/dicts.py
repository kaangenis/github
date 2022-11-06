from unicodedata import name


list_1 = ["adana", "ankara", "İstanbul"]
list_2 = [1, 6 , 34 ]

input_Deneme = input("Şehir adı giriniz: ")


if input_Deneme == "istanbul":
    plaka = list_2[list_1.index("İstanbul")]
    print(f"{input_Deneme} isimli şehrin plakası {plaka}")

elif input_Deneme == "adana":
    plaka = list_2[list_1.index("adana")]
    print(f"{input_Deneme} isimli şehrin plakası 0{plaka}")

elif input_Deneme == "ankara":
    plaka = list_2[list_1.index("ankara")]
    print(f"{input_Deneme} isimli şehrin plakası 0{plaka}")


#bu işlem iki adet liste ile yapıldı ama bunu tek bir dictionary ile yapmak çok daha kolay

dict_1 = {"kocaeli": 41, "istanbul": 34, "ankara": 6, "adana": 1}

dict_Deneme = input("Şehir Adı Giriniz: ")

if dict_Deneme == "istanbul":
    print(dict_1["istanbul"])

elif dict_Deneme == "ankara":
    print(dict_1["ankara"])

elif dict_Deneme == "adana":
    print(dict_1["adana"])

elif dict_Deneme == "kocaeli":
    print(f"{dict_Deneme} isimli şehrin plakası", dict_1["kocaeli"])


users = {
    "kaangenis": {
        "age": 20,
        "job": "student",
        "email": "kaang18@gmail.com",
        "phone number": "05313313131",
        "adress": "ankara, çankaya"
    },

    "yarenozkaya": {
        "age": 20,
        "job": "student",
        "email": "yarenozkaya@gmail.com",
        "phone number": "05313313132",
        "adress": "ankara, beytepe"

    }       

}

user_Input = input("username girin: ")

if user_Input == "kaangenis":
    age_Input = input("kaangenis hakkında sorunuz: ")

if age_Input == "age":
    print(users["kaangenis"]["age"])

elif user_Input == "yarenozkaya":
    print(users["yarenozkaya"])


