import config as cf
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import mergesort as mer
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime


#Cambio: Se modifico el catalogo con el fin de hacer uso de los mapas.Solo
#        se usaron para ello videosIds, categoryIds, tags y countries dado que 
#        las otras partes del catalogo no son utilizadas para el desarrollo de 
#        los requerimientos.
def newCatalog():
    catalog = {'videos': None,
               'categories': None,
               'videoIds': None,
               'categoryIds':None,
               'tags':None,
               'countries':None} #Solo se van a usar estos para bajar la complejidad y disminuir el tiempo del catalogo (usar solo lo necesario)
    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['categories'] = lt.newList('ARRAY_LIST')
    catalog['videoIds'] = mp.newMap(376000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapVideoIds)
    catalog['categoryIds'] = mp.newMap(50,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareMapCategoryIds)
    catalog['tags'] = mp.newMap(376000,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareTags)
    catalog['countries'] = mp.newMap(10,
                                   maptype='CHAINING',
                                   loadfactor=4.0,
                                   comparefunction=compareCountries)          
    return catalog
#Nueva: Esta funcion compara las llaves del mapa de videoIds
def compareMapVideoIds(keyName, entry):
    idEntry = me.getKey(entry)
    if (keyName == idEntry):
        return 0
    elif (keyName > idEntry):
        return 1
    else:
        return -1
#Nueva: Esta funcion compara las llaves del mapa de categoryIds
def compareMapCategoryIds(id,entry):
    idEntry = me.getKey(entry)
    if (int(id) == int(idEntry)):
        return 0
    elif (int(id) > int(idEntry)):
        return 1
    else:
        return -1
#Nueva: Esta funcion compara las llaves del mapa de tags
def compareTags(keyname, tag):
    tagEntry = me.getKey(tag)
    if (keyname == tagEntry):
        return 0
    elif (keyname > tagEntry):
        return 1
    else:
        return -1
#Esta función es para el compare del req 1
def cmpVideosByViews(video1,video2):
    return (float(video1['views'])> float(video2['views']))
#Nueva: Esta funcion compara las llaves del mapa de countries
def compareCountries(keyname, country):
    countryEntry = me.getKey(country)
    if (keyname == countryEntry):
        return 0
    elif (keyname > countryEntry):
        return 1
    else:
        return -1
#Nueva: Esta funcion añade un video del catalogo a la lista de videos y a los mapas.
#       Directamente en esta funcion solo añade video al map de videoIds, para los demas
#       se llama a otras funciones.
def addVideo(catalog, video):
    lt.addLast(catalog["videos"], video)
    mp.put(catalog['videoIds'], video['video_id'],video)
    tags = video['tags'].split('|')
    country = video['country']
    categoryId = video['category_id']
    addCountryVideo(catalog,country,video)
    addCategoryIdVideo(catalog,categoryId,video)
    for tag in tags:
        addTagVideo(catalog,tag.replace('"', ""),video)
#Nueva: Se usa en addViveo. Se añade el video al mapa de countries si ya esta en la lista ? 
#       si no recurre a otra funcion, lo crea y lo añade.
def addCountryVideo(catalog,countryName,video):
    countries = catalog['countries']
    if mp.contains(countries,countryName):
        entry = mp.get(countries,countryName)
        country = me.getValue(entry) 
    else:
        country = newCountry(countryName)
        mp.put(countries,countryName,country)
    lt.addLast(country['videos'],video)
#Nueva: Se usa en assCountryVideo. ??
def newCountry(countryName):
    country = {'name':"",
           'videos':None}
    country['name'] = countryName
    country['videos'] = lt.newList('ARRAY_LIST', compareCountries)
    return country

#Req 1
#Nueva: extrae el valor de una pareja en el mapa de countries.
def buscarcategoria(categoria,catalog):
    i=0
    while i<=mp.size(catalog['categories']):
        tempelement=lt.getElement(catalog['categories'],i)
        if tempelement['name']==str(" "+categoria):
            return tempelement['id']
        i+=1
    return i
def getMostViewedVideosByCountryAndCategory(catalog,pais,id_categoria,numero_videos):
    tad=lt.newList()
    cont=mp.get(catalog['categoryIds'],id_categoria) #Esta la pareja de llave,valor y luego #Esta es la lista
    cant=me.getValue(cont)['videos'] #.keys() 
    videos=it.newIterator(cant) #sacamos lista
    while it.hasNext(videos):
        video=it.next(videos)
        if video['country']==pais:
            lt.addLast(tad,video)
    mer.sort(tad,cmpVideosByViews)
    b=lt.subList(tad,1,int(numero_videos))
    return b
#Req 2
#Nueva: Se añade el video al mapa de categoryIds.
#Nueva: extrae el valor de una pareja en el mapa de countries.
def getVideoWithMostTrendingDaysByCountry(catalog,country):
    cot=mp.get(catalog['countries'],country)
    cat=me.getValue(cot)['videos']
    videos=it.newIterator(cat) #sacamos lista 
    respuesta=None
    cont=0
    while it.hasNext(videos):
        video=it.next(videos)
        cint=0
        while it.hasNext(videos):
            video2=it.next(videos)
            if video['video_id']==video2['video_id']:
                cint+=1
        if cint>cont:
            cont=cint
            respuesta=video
    return video
#Req 3
#Cambio(Nueva)
def getCategory(catalog, categoryId):
    category = mp.get(catalog['categoryIds'], categoryId)
    if category:
        return me.getValue(category)
    return None
def getVideoWithMostTrendingDaysByCategory(catalog, categoryId):
    category=mp.get(catalog['categoryIds'],categoryId)
    cot=me.getValue(category)['videos']
    videos=it.newIterator(cot)
    respuesta=None
    cont=0
    while it.hasNext(videos):
        video=it.next(videos)
        cint=0
        while it.hasNext(videos):
            video2=it.next(videos)
            if video['video_id']==video2['video_id']:
                cint+=1
        if cint>cont:
            cont=cint
            respuesta=video
    return video
#Req 4
#Cambio(Nueva)
def getTag(catalog, tagName):
    tag = mp.get(catalog['tags'], tagName)
    if tag:
        return me.getValue(tag)
    return None
#Para sortbyLikes
def compareLikes(video1, video2):
    return (int(video1['likes']) > int(video2['likes']))
#Cambio
def sortVideosByLikes(videos):
    lst = videos
    sa.sort(lst, compareLikes)
    return lst

def emptyList():
    return lt.newList('ARRAY_LIST')
def getMostLikedVideosByCountryAndTag(catalog, country, tag, n):
    tae=mp.get(catalog['tags'],tag)
    tv=me.getValue(tae)['videos']
    lis=sortVideosByLikes(tv)
    lst=emptyList()
    count=0
    videos=it.newIterator(lis)
    respuesta=None
    cont=0
    while it.hasNext(videos):
        video=it.next(videos)
        if cont< int(n):
            if video['country']==country:
                cont+=1
                lt.addLast(lst,video)
    print(lst)
    return lst
  

def addCategoryIdVideo(catalog,categoryId,video):
    categories = catalog['categoryIds']
    if mp.contains(categories,categoryId):
        entry = mp.get(categories,categoryId)
        category = me.getValue(entry) 
    else:
        category = newCategory(categoryId)
        mp.put(categories,categoryId,category)
    lt.addLast(category['videos'],video)
#Cambio(Nueva)
def newCategory(categoryId):
    category = {'id':0,
           'videos':None}
    category['id'] = categoryId
    category['videos'] = lt.newList('ARRAY_LIST', compareCountries)
    return category

#Nueva: Se añade el video al mapa de tags.
def addTagVideo(catalog,tagName,video):
    tags = catalog['tags']
    if mp.contains(tags,tagName):
        entry = mp.get(tags,tagName)
        tag = me.getValue(entry) 
    else:
        tag = newTag(tagName)
        mp.put(tags,tagName,tag)
    lt.addLast(tag['videos'],video)
#Cambio(Nueva)
def newTag(tagName):
    tag = {'name':"",
           'videos':None}
    tag['name'] = tagName
    tag['videos'] = lt.newList('ARRAY_LIST', compareTags)
    return tag



def addCategory(catalog, category):
    lt.addLast(catalog["categories"], category)


def getFirstVideo(catalog):
    return lt.firstElement(catalog["videos"])

# def getTrendingDays(video):
#     publishTimeString = video['publish_time'].split("-")
#     publishTime = datetime.datetime(int(
#         publishTimeString[0]), int(publishTimeString[1]), int(publishTimeString[2][0:2]))
#     trendingDateString = video['trending_date'].split(".")
#     trendingDate = datetime.datetime(int(
#         "20"+trendingDateString[0]), int(trendingDateString[2]), int(trendingDateString[1]))
#     return (trendingDate - publishTime).days
#Cambio
def getTrendingDays(video, catalog):
    ls = emptyList()
    count = 0
    for v in lt.iterator(catalog['videos']):
        if v['video_id']==video['video_id']:
            a = v['trending_date']
            if a not in ls:
                lt.addLast(ls, a)
                count=+1
    return(count)


def compareViews(video1, video2):
    return (int(video1['views']) > int(video2['views']))



#Cambio: Antes se pasaba el catalogo, ahora no es necesario.
def sortVideosByViews(videos):
    lst = videos
    sa.sort(lst, compareViews)
    return lst


