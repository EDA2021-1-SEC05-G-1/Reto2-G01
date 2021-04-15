import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


def printMenu():
    print("*"*asteriskNumber)
    print("Bienvenido")
    print("1- Cargar informacion en el catalogo")
    print("2- N videos con mas views tendencia en un pais por categoria")#REQ.1
    print("3- Video trending por mas dias en un pais")#REQ2
    print("4- Video trending por mas dias por categoria")#REQ3
    print("5- N videos con mas likes por pais con un tag en especifico")#REQ4
    print("6- Salir")
    print("*"*asteriskNumber)


catalog = None
asteriskNumber = 60


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        print("*"*asteriskNumber)
        catalog = controller.newCatalog()
        answer_1=controller.loadData(catalog)
        print("Se cargaron " + str(lt.size(catalog["videos"])) + " videos.")
        print("*"*asteriskNumber)
        firstElement = controller.getFirstVideo(catalog)
        print("Informacion del primer video")
        print("*"*asteriskNumber)
        print("title: "+firstElement["title"])
        print("channel_title: "+firstElement["channel_title"])
        print("trending_date: "+firstElement["trending_date"])
        print("country: "+firstElement["country"])
        print("views: "+firstElement["views"])
        print("likes: "+firstElement["likes"])
        print("dislikes: "+firstElement["dislikes"])
        print("*"*asteriskNumber)
        print("Categorias")
        print("*"*asteriskNumber)
        for category in lt.iterator(catalog["categories"]):
            print(category['id']+": "+category['name'])
        print("Tiempo [ms]: ", f"{answer_1[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer_1[1]:.3f}")
    elif int(inputs[0]) == 2:
        category = input('Ingrese la categoria:\n')
        country = input('Ingrese el pais (country):\n')
        n = input('Numeros de videos a listar:\n')
        category=controller.buscarcategoria(category,catalog)
        answer_2 = controller.getMostViewedVideosByCountryAndCategory(
            catalog, country, category, n)
        videosByCountry=answer_2[0]
        for video in lt.iterator(videosByCountry):
            print("*"*asteriskNumber)
            print('trending_date: '+video['trending_date'])
            print('title: '+video['title'])
            print('publish_time: '+video['publish_time'])
            print('views: '+video['views'])
            print('likes: '+video['likes'])
            print('dislikes: '+video['dislikes'])
        print("Tiempo [ms]: ", f"{answer_2[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer_2[2]:.3f}")
    elif int(inputs[0]) == 3:
        country = input('Ingrese el pais (country):\n')
        answer_3 = controller.getVideoWithMostTrendingDaysByCountry(
            catalog, country)
        video_1=answer_3[0]
        if video_1==None:
            print("No hay video que cumpla con estas caracteristicas")
        else: 
            print("*"*asteriskNumber)
            print("title: "+video_1['title'])
            print("channel_title: "+video_1['channel_title'])
            print("country: "+video_1['country'])
            print("Días: "+str(controller.getTrendingDays(video_1,catalog)))
        print("Tiempo [ms]: ", f"{answer_3[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer_3[2]:.3f}")
    elif int(inputs[0]) == 4:
        category = input('Ingrese la categoria:\n')
        category=controller.buscarcategoria(category,catalog)
        answer_4 = controller.getVideoWithMostTrendingDaysByCategory(
            catalog, category)
        video_2=answer_4[0]
        if video_2==None:
            print("No hay video que cumpla con estas caracteristicas")
        else: 
            print("*"*asteriskNumber)
            print("title: "+video_2['title'])
            print("channel_title: "+video_2['channel_title'])
            print("category_id: "+video_2['category_id'])
            print("Días: "+str(controller.getTrendingDays(video_2,catalog)))
        print("Tiempo [ms]: ", f"{answer_4[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer_4[2]:.3f}")
    elif int(inputs[0]) == 5:
        country = input('Ingrese el pais (country):\n')
        tag = input('Ingrese el tag:\n')
        n = int(input('Numeros de videos a listar:\n'))
        answer_5 = controller.getMostLikedVideosByCountryAndTag(
            catalog, country, tag, n)
        videosTag=answer_5[0]
        for video_3 in lt.iterator(videosTag):
            print("*"*asteriskNumber)
            print("Title: "+video_3['title'])
            print("channel_title: "+video_3['channel_title'])
            print("publish_time: "+video_3['publish_time'])
            print("views: "+video_3['views'])
            print("likes: "+video_3['likes'])
            print("dislikes: "+video_3['dislikes'])
            print("tags: "+video_3['tags'])
        print("Tiempo [ms]: ", f"{answer_5[1]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer_5[2]:.3f}")
    else:
        sys.exit(0)
sys.exit(0)

