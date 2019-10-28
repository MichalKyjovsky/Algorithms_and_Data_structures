class Graph:
    def __init__(self,V):
        self.V = V
        self.adj = [[] for i in range(V)] #adjacency list

    def addEdge(self,u,v):
        self.adj[u].append(v)   #Add v to u's list

    def DFS(self,s):
        visited = [False for i in range(self.V)]
        stack = []
        stack.append(s)

        while(len(stack)):
            s = stack[-1] # pop from stack
            stack.pop()

            if(not visited[s]):
                print(s,' ')
                visited[s] = True

            for node in self.adj[s]:
                if (not visited[node]):
                    stack.append(node)

g = Graph(10)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(3,4)
g.addEdge(5,3)
g.addEdge(0,3)
g.addEdge(6,0)
g.addEdge(9,6)
g.addEdge(8,6)
g.addEdge(6,7)
g.addEdge(0,9)
g.addEdge(6,3)

print('DFS result')
g.DFS(0)

