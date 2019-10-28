#Ford Fulkerson algorithm implemenatation

from collections import defaultdict

#This class represents a direct graph using adjacency matrix representation
class Graph:

    def __init__(self,graph):
        self.graph = graph
        self.row = len(graph)

    '''Returns true if there is a path from source 's' to sink 't' in 
     residual graph. Also fills paren[] to store the path '''
    def BFS(self,s,t,parent):

        #Mark all the vertices as not visited
        visited =[False]*self.row

        #Create a queue for BFS
        queue=[]

        #Mark the source node as a visited at enqueue it
        queue.append(s)
        visited[s] = True

        #Standard BFS loop
        while queue:

            #Dequeue a vertex from queue and print it
            u = queue.pop(0)

            #Get all adjacent verticies of the dequeued vertex u
            #If adjacent has not been visited, than mark it
            #visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0 :
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

            #If we reached the sink in BFS starting from source, then return
            # true, else false
        return True if visited[t] else False

    #Returns the maximum flow from s to t in the given graph
    def FordFulkerson(self,source,sink):

        #This array is filled by BFS and to store the path
        parent = [-1]*(self.row)

        #There is no flow initially
        max_flow = 0

        #Augment the flow while there is the path from source to sink
        while self.BFS(source, sink, parent):

            #FInd the residual capacity of the edges along the
            #path filled by BFS. Or we can say find maximum flow
            #through the path found
            path_flow = float("Inf")
            s = sink

            while(s !=source):
                path_flow = min (path_flow, self.graph[parent[s]][s])
                s = parent[s]

            #Add path flow to overall flow
            max_flow += path_flow

            #Update residual capacities of the edges and reverse edges
            #along the path
            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow

graph = [[0,10,10,0,0,0],
         [0,0,0,7,5,0],
         [0,0,0,9,3,0],
         [0,0,0,0,0,10],
         [0,0,0,0,0,10],
         [0,0,0,0,0,0]]

g = Graph(graph)
source = 0; sink = 5

print("The maximum possible flow is %d " % g.FordFulkerson(source,sink))
