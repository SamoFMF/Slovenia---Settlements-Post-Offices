# Using google maps api (distance matrix)
import requests
from datastructure import Entry
from utils import saveFile, loadFile, coordToDeg
from typing import List
from create_pajek_graphs import distToGraph

key = ""
with open("mykey.env", "r") as f:
    key = f.readline().rstrip("\n")

def createLink(origins: List[Entry], destinations: List[Entry], key: str) -> str:
    link = "https://maps.googleapis.com/maps/api/distancematrix/json?origins="
    for i in range(len(origins)):
        lon, lat = origins[i].coordinates
        link += f"{coordToDeg(lat)},{coordToDeg(lon)}"
        if i+1 < len(origins):
            link += "|"
    link += "&destinations="
    for i in range(len(destinations)):
        lon, lat = destinations[i].coordinates
        link += f"{coordToDeg(lat)},{coordToDeg(lon)}"
        if i+1 < len(destinations):
            link += "|"
    link += "&key="
    link += key
    return link

if __name__ == "__main__":
    D = loadFile("data/distances10.pkl.gz")
    data,_ = loadFile("data/naselja_poste.pkl.gz")
    G = distToGraph(D)

    print("START REQUESTS")
    istart = 5500
    iend = len(G)
    results = []
    for i in range(istart, iend):
        if i%10 == 0: print(i)
        origins = [data[i]]
        destinations = [data[j] for j,_ in G[i] if j>i]
        if len(destinations) > 0:
            results.append(requests.post(createLink(origins, destinations, key)).json())
            if results[-1]["status"] != "OK":
                print(f"ERROR at i={i}")
                break
        else:
            # add empty result
            results.append(None)
    print("SAVING FILE")
    saveFile(f"gmaps_raw/distances_gmaps_{istart:04d}_{iend:04d}.pkl.gz", results)
    print("DONE")