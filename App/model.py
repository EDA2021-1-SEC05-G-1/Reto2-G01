import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
import datetime




def newCatalog():
    
    catalog = {'videos': None,
               'videosIds': None,
               'country': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'trending_date': None,
               'publish_time': None,
               'categories': None}
    
    catalog['videos'] = lt.newList()
    catalog['categories'] = lt.newList()
    catalog['videosIds'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareVideosIds)
    catalog['country'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareCountry)
    catalog['views'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareViews)
    catalog['likes'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareLikes)
    catalog['dislikes'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareDislikes)
    catalog['trending_date'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareTrendingDate)
    catalog['publish_time'] = mp.newMap(34500,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=comparePublishTime)       
    return catalog
# ==============================
# Funciones de Comparacion
# ==============================


def compareVideosIds(id1, id2):
    """
    Compara dos ids de dos videos
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareCountry (id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compareViews(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareLikes(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareDislikes(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def compareTrendingDate(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
def comparePublishTime(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1
        
def buscacategoria(categoria,catalog):
    i=0
    mp.get()
    me.getValue()
    mp.Keyset()
    while i<=mp.size(catalog['categories']):
        tempelement=lt.getElement(catalog['categories'],i)
        if tempelement['name']==str(" "+categoria):
            return int(tempelement['id'])
        i+=1
    return i
def filtrada(catalog,pais,id_categoria,numero_videos):
    tad=lt.newList('ARRAY_LIST')
    lista_n=[]
    i=1
    while i< (lt.size(catalog['videos'])):
        if (pais in (lt.getElement(catalog['videos'],i)['country'])) and (str(id_categoria) in (lt.getElement(catalog['videos'],i)['category_id'])):
            lt.addLast(tad,lt.getElement(catalog['videos'],i))
        i+=1
    a=tad.copy()
    mer.sort(a,cmpVideosByViews)
    b=lt.subList(a,1,numero_videos)
    return b

def emptyList():
    return lt.newList('ARRAY_LIST')


def addVideo(catalog, video):
    lt.addLast(catalog["videos"], video)


def addCategory(catalog, category):
    lt.addLast(catalog["categories"], category)


def getFirstVideo(catalog):
    return lt.firstElement(catalog["videos"])


def getVideosByCountry(catalog, country):
    countryList = mp.get(catalog['videos'], country)
    if countryList:
        return me.getValue(countryList)
    return None


def getTrendingDays(video):
    publishTimeString = video['publish_time'].split("-")
    publishTime = datetime.datetime(int(
        publishTimeString[0]), int(publishTimeString[1]), int(publishTimeString[2][0:2]))
    trendingDateString = video['trending_date'].split(".")
    trendingDate = datetime.datetime(int(
        "20"+trendingDateString[0]), int(trendingDateString[2]), int(trendingDateString[1]))
    return (trendingDate - publishTime).days



def compareTrendingDays(video1, video2):
    return (getTrendingDays(video1) > getTrendingDays(video2))


def compareLikes(video1, video2):
    return (int(video1['likes']) > int(video2['likes']))


def sortVideosByViews(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareViews)
    return lst


def sortVideosByTrendingDays(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareTrendingDays)
    return lst


def sortVideosByLikes(catalog):
    lst = catalog['videos']
    sa.sort(lst, compareLikes)
    return lst
