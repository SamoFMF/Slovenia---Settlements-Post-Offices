# Sort cities by distance from each settlement
from pickle import load
from utils import loadFile, saveFile, coordToDeg, getDistance
from time import time

data, centers = loadFile("data/naselja_poste.pkl.gz")

# t = time()
# D = [list() for _ in range(len(data))]
# for i in range(len(data)):
#     if i%100 == 0: print(i)
#     for j in range(i+1, len(data)):
#         dist = getDistance(data[i].coordinates, data[j].coordinates)
#         D[i] += [(dist, j)]
#         D[j] += [(dist, i)]
# for i in range(len(D)):
#     D[i].sort()

# # Uncomment to save
# saveFile("data/distances.pkl.gz", D)

# D = loadFile("data/distances100.pkl.gz")
# D15 = [d[:15] for d in D]
# saveFile("data/distances15.pkl.gz", D15)

# D10 = [d[:10] for d in D]
# saveFile("data/distances10.pkl.gz", D10)