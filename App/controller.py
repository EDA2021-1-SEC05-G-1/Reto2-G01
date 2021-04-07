import config as cf
from DISClib.ADT import list as lt
import model
import csv
import time
import tracemalloc


def newCatalog():
    catalog = model.newCatalog()
    return catalog


def loadData(catalog):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()

    loadVideos(catalog)
    loadCategories(catalog)

    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return delta_time, delta_memory
    


def loadVideos(catalog):
    videoFile = cf.data_dir+'videos-small.csv'
    inputFile = csv.DictReader(open(videoFile, encoding="utf-8"))
    for video in inputFile:
        model.addVideo(catalog, video)


def loadCategories(catalog):
    categoryFile = cf.data_dir+'category-id.csv'
    inputFile = csv.DictReader(open(categoryFile, encoding="utf-8"),delimiter='\t')
    for category in inputFile:
        model.addCategory(catalog, category)
    

def getFirstVideo(catalog):
    return model.getFirstVideo(catalog)


def getMostViewedVideosByCountryAndCategory(catalog, country, categoryId, n):
    lst = model.sortVideosByViews(catalog)
    emptyLst = model.emptyList()
    count = 0
    for video in lt.iterator(lst):
        if(count < int(n)):
            if(video['country'] == country and video['category_id'] == categoryId):
                lt.addLast(emptyLst, video)
                count += 1
    return emptyLst


def getVideoWithMostTrendingDaysByCountry(catalog, country):
    lst = model.sortVideosByTrendingDays(catalog)
    for video in lt.iterator(lst):
        if(video['country'] == country):
            return video


def getVideoWithMostTrendingDaysByCategory(catalog, categoryId):
    lst = model.sortVideosByTrendingDays(catalog)
    for video in lt.iterator(lst):
        if(video['category_id'] == categoryId):
            return video


def getTrendingDays(video):
    return model.getTrendingDays(video)


def getMostLikedVideosByCountryAndTag(catalog, country, tag, n):
    lst = model.sortVideosByLikes(catalog)
    emptyLst = model.emptyList()
    count = 0
    for video in lt.iterator(lst):
        if(count <= int(n)):
            if(video['country'] == country):
                hasTag = False
                for tagItem in video['tags'].split('|'):
                    finalTag = tagItem.replace('"', "")
                    if(finalTag == tag):
                        hasTag = True
                if(hasTag):
                    lt.addLast(emptyLst, video)
                    count += 1
    return emptyLst

def getMostLikedVideos(catalog,n):
  lst = model.sortVideosByLikes(catalog)
  emptyLst = model.emptyList()
  count = 0 
  for video in lt.iterator(lst):
        if(count <= int(n)):
            lt.addLast(emptyLst, video)
            count += 1
        return emptyLst


# ======================================
# Funciones para medir tiempo y memoria
# ======================================


def getTime():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)



def getMemory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def deltaMemory(start_memory, stop_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
