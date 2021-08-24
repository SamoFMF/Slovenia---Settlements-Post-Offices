# We create 2 different networks:
#   1. using distances from gmaps
#   2. using times from gmaps
from utils import loadFile, saveFile
from datastructure import Entry
from create_pajek_graphs import distToGraph
from os import listdir, path
from typing import List, Tuple

def mergeResults(_path: str = "gmaps_raw") -> List[dict]:
    result = []
    for filename in listdir(_path):
        result += loadFile(path.join(_path, filename))
    print(len(result))
    return result

def createGraphs(rawData: List[dict], Graw: List[List[tuple]], n: int) -> Tuple[List[List[tuple]]]:
    Gdist = [[] for _ in range(n)]
    Gtime = [[] for _ in range(n)]
    for i in range(len(rawData)): # TODO: Replace with n, when distances is complete
        data = rawData[i]
        if data is None:
            # print("data is None:", i)
            continue
        if data["status"] != "OK":
            # ERROR
            print("ERROR in line:", i)
            continue
        data = data["rows"][0]["elements"]
        valid = [j for j,_ in Graw[i] if j>i]
        if len(data) != len(valid):
            print("ERROR count:", i)
        for j in range(len(valid)):
            dataj = data[j]
            if dataj["status"] != "OK":
                print("ERROR in line:", i, j)
                continue
            u = valid[j]
            dist = dataj["distance"]["value"]
            dur = dataj["duration"]["value"]
            Gdist[i].append((u,dist))
            Gtime[i].append((u,dur))
            Gdist[u].append((i,dist))
            Gtime[u].append((i,dur))
    return Gdist, Gtime

if __name__ == "__main__":
    rawData = mergeResults("gmaps_raw")
    D = loadFile("data/distances10.pkl.gz")
    G = distToGraph(D)

    Gdist, Gtime = createGraphs(rawData, G, len(G))
    print(sum(len(i) for i in Gdist) // 2)
    print(sum(len(i) for i in Gtime) // 2)
    saveFile("gmaps/gmaps_distances10.pkl.gz", Gdist)
    saveFile("gmaps/gmaps_durations10.pkl.gz", Gtime)