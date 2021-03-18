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
               'dislikes': None
               'trending_date': None
               'publish_time': None
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


def compareViews(video1, video2):
    return (int(video1['views']) > int(video2['views']))


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
