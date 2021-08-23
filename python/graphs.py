# Graphical representations
from utils import loadFile, coordToDeg
import matplotlib.pyplot as plt

def drawMap(fig, data, color="b", scale=None):
    xs = [coordToDeg(d.coordinates[0]) for d in data]
    ys = [coordToDeg(d.coordinates[1]) for d in data]
    if scale is None:
        fig.scatter(xs, ys, c=color)
    else:
        fig.scatter(xs, ys, c=color, s=scale)

data = loadFile("data/naselja.pkl.gz")
pop = [d.population for d in data]
maxp = max(pop)
scale = [50 * (p/maxp) for p in pop]
drawMap(plt, data, "b", scale)
plt.show()

data, centers = loadFile("data/naselja_poste.pkl.gz")
datac = [data[i] for i in centers]

pop = [d.population for d in data]
maxp = max(pop)
popc = [pop[i] for i in centers]
maxpc = max(popc)

scale = [50 * (p/maxp) for p in pop]
scalec = [50 * (pc/maxpc) for pc in popc]

drawMap(plt, data, "b", scale)
drawMap(plt, datac, "r", scalec)
# plt.savefig("slovenia.pdf")
plt.show()