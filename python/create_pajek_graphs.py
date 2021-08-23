# This script creates Pajek files representing different datasets
# It is similar to Pajek, but not exactly the same
from utils import loadFile, saveFile
from datastructure import Entry

'''
*vertices n
1 label1 weight1
2 label2 weight2
...
n labeln weightn
*edges
i j w_{i,j}
'''
def getPajek(filename, G, wnodes=None, labels=None):
    with open(filename, "w") as f:
        f.write(f"*vertices {len(G)}\n")
        for i in range(len(G)):
            line = f'{i+1} "{labels[i] if labels is not None else i+1}"'
            if wnodes is not None:
                line += f" {wnodes[i]}"
            f.write(line + "\n")
        f.write(f"*edges {sum(len(i) for i in G) // 2}\n")
        for i in range(len(G)):
            # G[i].sort(key=lambda x: x[1])
            for j,v in G[i]:
                if i < j:
                    f.write(f"{i+1} {j+1} {v}\n")

def distToGraph(D):
    # Makes sure that if j in G[i], then i in G[j]
    # Also makes sure that G[i] is sorted by nodes, not distances
    edges = set()
    G = [[] for _ in range(len(D))]
    for i in range(len(D)):
        for v,j in D[i]:
            tmp = (i,j) if i<j else (j,i)
            if tmp in edges:
                continue
            else:
                edges.add(tmp)
                G[i].append((j,v))
                G[j].append((i,v))
    for i in range(len(G)):
        G[i].sort()
    return G

# D = loadFile("data/distances.pkl.gz")
# print("Done reading")
# for i in range(len(D)):
#     if i%100 == 0: print(i)
#     D[i].sort(key=lambda x: (x[1],x[0]))
# print("Done sorting")

if __name__ == "__main__":
    D = loadFile("data/distances10.pkl.gz")

    data, centers = loadFile("data/naselja_poste.pkl.gz")
    wnodes = [d.population for d in data]

    # with open("graphs/slovenia_post_offices.net", "w") as f:
    #     f.write(f"{len(centers)}\n")
    #     centers.sort()
    #     for c in centers:
    #         f.write(f"{c}\n")

    # names are in the following format:
    #   slovenia_d_{distance used}_{wnodes!=None}_{labels!=None}.net
    #   example: "graphs/slovenia_d_full_0_0.net"
    getPajek("graphs/slovenia_d_10_1_0.net", distToGraph(D), wnodes)