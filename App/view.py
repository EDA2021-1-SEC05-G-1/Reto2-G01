import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp


def printMenu():
    print("*"*asteriskNumber)
    print("Bienvenido")
    print("1- Cargar informacion en el catalogo")
    print("2- N videos con mas views tendencia en un pais por categoria")
    print("3- Video trending por mas dias en un pais")
    print("4- Video trending por mas dias por categoria")
    print("5- N videos con mas likes por pais con un tag en especifico")
    print("6- N videos con mas likes")
    print("7- Salir")
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
        controller.loadData(catalog)
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
        answer = controller.loadData(catalog)
        for category in lt.iterator(catalog['categories']):
            print(category['id'] + category['name'])
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")
    elif int(inputs[0]) == 2:
        category = input('Ingrese la categoria (category_id):\n')
        country = input('Ingrese el pais (country):\n')
        n = input('Numeros de videos a listar:\n')
        videosByCountry = controller.getMostViewedVideosByCountryAndCategory(
            catalog, country, category, n)
        for video in lt.iterator(videosByCountry):
            print("*"*asteriskNumber)
            print('trending_date: '+video['trending_date'])
            print('title: '+video['title'])
            print('publish_time: '+video['publish_time'])
            print('views: '+video['views'])
            print('likes: '+video['likes'])
            print('dislikes: '+video['dislikes'])
    elif int(inputs[0]) == 3:
        country = input('Ingrese el pais (country):\n')
        video = controller.getVideoWithMostTrendingDaysByCountry(
            catalog, country)
        print("*"*asteriskNumber)
        print("title: "+video['title'])
        print("channel_title: "+video['channel_title'])
        print("country: "+video['country'])
        print("Días: "+str(controller.getTrendingDays(video)))
    elif int(inputs[0]) == 4:
        category = input('Ingrese la categoria (category_id):\n')
        video = controller.getVideoWithMostTrendingDaysByCategory(
            catalog, category)
        print("*"*asteriskNumber)
        print("title: "+video['title'])
        print("channel_title: "+video['channel_title'])
        print("category_id: "+video['category_id'])
        print("Días: "+str(controller.getTrendingDays(video)))
    elif int(inputs[0]) == 5:
        country = input('Ingrese el pais (country):\n')
        tag = input('Ingrese el tag:\n')
        n = input('Numeros de videos a listar:\n')
        videosTag = controller.getMostLikedVideosByCountryAndTag(
            catalog, country, tag, n)
        for video in lt.iterator(videosTag):
            print("*"*asteriskNumber)
            print("Title: "+video['title'])
            print("channel_title: "+video['channel_title'])
            print("publish_time: "+video['publish_time'])
            print("views: "+video['views'])
            print("likes: "+video['likes'])
            print("dislikes: "+video['dislikes'])
            print("tags: "+video['tags'])
    elif int(inputs[0]) == 6:
        n = input('Numeros de videos a listar:\n')
        videos = controller.getMostLikedVideos(catalog, n)
        for video in lt.iterator(videos):
            print("*"*asteriskNumber)
            print("Title: "+video['title'])
            print("channel_title: "+video['channel_title'])
            print("publish_time: "+video['publish_time'])
            print("views: "+video['views'])
            print("likes: "+video['likes'])
            print("dislikes: "+video['dislikes'])
            print("tags: "+video['tags'])
    else:
        sys.exit(0)
sys.exit(0)