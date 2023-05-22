import random
import numpy as np

adj = []
for i in range(4):
    adj.append(random.sample(range(100),4))
    
for i in range(len(adj)):
    for j in range(len(adj[i])):
        if i==j:
            adj[i][j]=999

print(np.array(adj))
start = int(input())
visited = []
dist = 0
visited.append(start)
dist+=min(adj[visited[-1]])
while list(set(visited))!=[i for i in range(len(adj))]:
    for i in range(len(adj)):
        adj[i][visited[-1]]=999
    nxt = adj[visited[-1]].index(min(adj[visited[-1]]))
    dist+=min(adj[visited[-1]])
    print(np.array(adj))
    print(nxt)
    visited.append(nxt)
    continue
    
print(visited)
