# Every search including 'Kneške Ravne' was broken
from utils import loadFile, saveFile

def createDict(dtext, dval, ttext, tval):
    return {'distance': {'text': dtext, 'value': dval},
            'duration': {'text': ttext, 'value': tval},
            'status': 'OK'}

res = loadFile("gmaps_raw_unedited/distances_gmaps_1100_2000_unedited.pkl.gz")

# Fix node 1841 (Kneške Ravne)
probName = 'Kneške Ravne, 5216 Most na Soči, Slovenia'
dests = ['Lisec 1, 5216 Most na Soči, Slovenia', 'Loje 8, 5216 Most na Soči, Slovenia', 'Podmelec, 5216, Slovenia', 'Rut 43, 5242 Grahovo ob Bači, Slovenia', 'Sela nad Podmelcem 13-15, 5220 Tolmin, Slovenia', 'Temljine 35, 5242 Grahovo ob Bači, Slovenia', 'Tolminske Ravne 14, 5220 Tolmin, Slovenia', 'Ukanc 40-42, 4265 Bohinjsko jezero, Slovenia', 'Zadlaz - Čadrg 11, 5220 Tolmin, Slovenia', 'Zadlaz - Žabče, 5220, Slovenia']
origins = [probName]
elements = [createDict('7.1 km', 7100, '36 mins', 2160),
            createDict('13.8 km', 13800, '48 mins', 2880),
            createDict('12.0 km', 12000, '44 mins', 2640),
            createDict('22.4 km', 22400, '1 hour 1 min', 3660),
            createDict('22.7 km', 22700, '1 hour 7 mins', 4020),
            createDict('13.2 km', 13200, '47 mins', 2820),
            createDict('35.2 km', 35200, '1 hour 21 mins', 4860),
            createDict('63.3 km', 63300, '2 hours 1 min', 7260),
            createDict('29.2 km', 29200, '1 hour 8 mins', 4080),
            createDict('27.9 km', 27900, '1 hour 4 mins', 3840)]

res[741]["destination_addresses"] = dests
res[741]["origin_addresses"] = origins
res[741]["rows"][0]["elements"] = elements

# Fix node 1330 (connected to 1841)
res[230]["destination_addresses"][1] = probName
res[230]["rows"][0]["elements"][1] = createDict('23.9 km', 23900, '1 hour 4 mins', 3840)

saveFile("gmaps_raw/distances_gmaps_1100_2000.pkl.gz", res)