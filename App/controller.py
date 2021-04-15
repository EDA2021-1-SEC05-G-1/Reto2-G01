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
    videoFile = cf.data_dir+'videos-large.csv'
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

##REQ1
#Cambio: Antes se hacia un filtro, creando una lista del pais a partir del catalogo, 
#        ahora no es necesario. 
#        Sería la complejidad del for mas la complejidad del sort. merge+tamaño de lst -OJO:While
def buscarcategoria(category,catalog):
    return model.buscarcategoria(category,catalog)
#Req 1
def getMostViewedVideosByCountryAndCategory(catalog, country, categoryId, n):
    
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    devuelve=model.getMostViewedVideosByCountryAndCategory(catalog,country,categoryId,n)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return devuelve,delta_time, delta_memory
    

##REQ2
#Cambio
#n^2- Tamaño de la lista-for anidado
def getVideoWithMostTrendingDaysByCountry(catalog, country):

    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    devuelve=model.getVideoWithMostTrendingDaysByCountry(catalog,country)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return devuelve,delta_time, delta_memory
    
    
##REQ3
# Cambio
def getVideoWithMostTrendingDaysByCategory(catalog, categoryId):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    devuelve=model.getVideoWithMostTrendingDaysByCategory(catalog, categoryId)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return devuelve,delta_time, delta_memory


def getTrendingDays(video,catalog):
    return model.getTrendingDays(video,catalog)
##REQ4
#Cambio
#Antes se organizaba todo el catalogo por likes y luego se debia comparar por país y por tag.
#sort+lst.
def getMostLikedVideosByCountryAndTag(catalog, country, tag, n):
    tracemalloc.start()
    start_time = getTime()
    start_memory = getMemory()
    devuelve=model.getMostLikedVideosByCountryAndTag(catalog, country, tag, n)
    stop_memory = getMemory()
    stop_time = getTime()
    tracemalloc.stop()

    delta_time = stop_time - start_time
    delta_memory = deltaMemory(start_memory, stop_memory)

    return devuelve,delta_time, delta_memory
    
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
