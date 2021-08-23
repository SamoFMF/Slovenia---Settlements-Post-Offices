# Test if graph with 15 closest settlements is connected
from utils import loadFile

D = loadFile("data/distances15.pkl.gz")

# G = [sorted(i[1] for i in d) for d in D]
G = [{i[1] for i in d} for d in D]

for u in range(len(G)):
    for v in G[u]:
        G[v].add(u)

print(sum(len(i) for i in G))

for u in range(len(G)):
    for v in G[u]:
        if u == v:
            print(u)

def getComponent(node):
    visited = {node}
    stack = [i for i in G[node]]
    while len(stack) > 0:
        node = stack.pop()
        if node in visited:
            continue
        else:
            visited.add(node)
        for i in G[node]:
            if i not in visited:
                stack.append(i)
    return visited

C = getComponent(0)
print(len(C))