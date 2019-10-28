# Python implementation of DFS algorithm

from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def DFSutil(self,v,visited):

        visited[v] = True
        print(v," ")

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSutil(i,visited)

    def DFS(self,v):

        visited = [False] * len(self.graph)

        self.DFSutil(v,visited)


g = Graph()
g.addEdge(0,1)
g.addEdge(0,5)
g.addEdge(4,0)
g.addEdge(1,4)
g.addEdge(4,0)
g.addEdge(3,4)
g.addEdge(3,2)
g.addEdge(2,0)
g.addEdge(2,1)
g.addEdge(5,3)

g.DFS(0)