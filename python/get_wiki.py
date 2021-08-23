# Gathers all Slovenian towns (settlements?)

from sys import stdin
from time import time
import pickle
import wikipedia
from datastructure import *
from utils import saveFile

disambigError = []
popError = []

language = "sl"

wikipedia.set_lang(language)

def createTable(x: str):
    ttotal = time()
    T = Table(wikipedia.page(f"Seznam_naselij_v_Sloveniji_({x.upper()})").html())
    T.extractData()
    print(f"Data with {len(T.data)} entries extracted in {round((time()-ttotal)*1000, 2)}ms.\n")

    ttotal = time()
    for entry in T.data:
        t = time()
        print(f"{entry.link} || {entry.municipality}")
        entry.updateData()
        print(entry.population)
        print(f"Time={round((time()-t)*1000, 2)}ms || Total time={round((time()-ttotal)*1000, 2)}ms.\n")
    
    return T

if __name__ == "__main__":
    # x = stdin.readline().rstrip("\n")
    for x in "p":
        print(f"\nNOVA ČRKA = {x}\n")
        T = createTable(x)

        saveFile(f"data/naselja_{x}.pkl.gz", T)