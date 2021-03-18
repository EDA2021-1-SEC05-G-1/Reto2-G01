import config as cf
from DISClib.ADT import list as lt
import model
import csv


def newCatalog():
    catalog = model.newCatalog()
    return catalog


def loadData(catalog):
    loadVideos(catalog)
    loadCategories(catalog)


def loadVideos(catalog):
    videoFile = cf.data_dir+'videos-small.csv'
    inputFile = csv.DictReader(open(videoFile, encoding="utf-8"))
    for video in inputFile:
        model.addVideo(catalog, video)


def loadCategories(catalog):
    categoryFile = cf.data_dir+'category-id.csv'
    inputFile = csv.DictReader(open(categoryFile, encoding="utf-8"))
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
