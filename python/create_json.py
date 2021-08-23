# Create JSON file containing Slovenian settlements
from os import replace
from utils import loadFile, saveFile, coordToDeg
import json
from datastructure import *
from typing import List, Tuple

def replaceLetters(string: str, letterPairs: List[Tuple[str, str]]) -> str:
    for a, b in letterPairs:
        string = string.replace(a, b)
    return string

class MyEncoder(json.JSONEncoder):
    def default(self, o: Entry) -> dict:
        tmp = o.__dict__.copy()

        # Fix coordinates
        lon,lat = tmp.pop("coordinates")
        tmp["latitude"] = coordToDeg(lat)
        tmp["longitude"] = coordToDeg(lon)

        # Fix post office
        tmp["postNumber"] = tmp.pop("idx")

        # Change č,š,ž to c,s,z
        tmp["title"] = tmp.pop("link")

        return tmp

class MyEncoderASCII(json.JSONEncoder):
    def default(self, o: Entry) -> dict:
        tmp = o.__dict__.copy()

        # Fix coordinates
        lon,lat = tmp.pop("coordinates")
        tmp["latitude"] = coordToDeg(lat)
        tmp["longitude"] = coordToDeg(lon)

        # Fix post office
        tmp["postNumber"] = tmp.pop("idx")

        # Change č,š,ž to c,s,z
        pairs = [("č","c"), ("š","s"), ("ž","z")]
        tmp["town"] = replaceLetters(tmp["town"], pairs)
        tmp["title"] = tmp.pop("link")
        tmp["title"] = replaceLetters(tmp["title"], pairs)
        tmp["municipality"] = replaceLetters(tmp["municipality"], pairs)
        tmp["municipalityTitle"] = replaceLetters(tmp["municipalityTitle"], pairs)
        tmp["statRegion"] = replaceLetters(tmp["statRegion"], pairs)
        tmp["region"] = replaceLetters(tmp["region"], pairs)

        return tmp

if __name__ == "__main__":
    data, _ = loadFile("data/naselja_poste.pkl.gz")

    # S šumniki
    with open("data/naselja.json", "w", encoding="utf-8") as f:
        json.dump(data, f, cls=MyEncoder, ensure_ascii=False, indent="\t")
    
    # ASCII
    with open("data/naselja_ascii.json", "w", encoding="utf-8") as f:
        json.dump(data, f, cls=MyEncoderASCII, ensure_ascii=True, indent="\t")