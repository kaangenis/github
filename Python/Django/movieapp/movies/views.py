from django.shortcuts import render

# Create your views here.

kategori_Liste = ["macera", "romantik", "dram", "komedi"]

film_Liste = [


    {
        "film_Adi": "Fight Club",
        "film_Turu": "Aksiyon, Felsefe",
        "film_Yonetmen" : "David Fincher",
        "film_Sure": "2 Saat 19 Dakika",
        "film_CikisYili": "1999",
        "film_Logo" : "https://www.themoviedb.org/t/p/w220_and_h330_face/yjMuqAyJUoQZGWsZ0vZuYj5inAR.jpg",
        "film_Anasayfa" : True

    },

    {
        "film_Adi": "Troy",
        "film_Turu": "Tarih, Mitoloji",
        "film_Yonetmen": "Wolfgang Petersen",
        "film_Sure" : "2 Saat 26 Dakika",
        "film_CikisYili": "2004",
        "film_Logo" : "troylogo.jpg",
        "film_Anasayfa" : True

    },

    {
        "film_Adi": "Focus",
        "film_Turu": "Macera, Romantik Komedi",
        "film_Yonetmen": "Glenn Ficarra",
        "film_Sure": "1 Saat 44 Dakika",
        "film_CikisYili": "2015",
        "film_Logo": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSt0fwVtAoBlesvBlxk0ytnPEztw7aTBJOr07ikiGydA8xaQq7YQDH-WCmAbyFZkEYy48E&usqp=CAU",
        "film_Anasayfa": True

    }

              ]


def home(request):

    data = {

        "kategoriler" : kategori_Liste

    }

    return render(request, "index.html", data)

def moviepage(request):

    data_2 = {

        "filmler": film_Liste


    }

    return render(request, "moviepage.html", data_2)
