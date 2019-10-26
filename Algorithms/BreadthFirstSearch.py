#Python implementation of BFS alg.
#from a given source vertex. BFS(int s)
#traverses vertices reachable from s.
from collections import defaultdict

#This class represents a directed graph
#using adjacency list represenation
class Graph: 
	
	#Constructor 
	def __init__(self):
		
		# default dictionary to store a graph
		self.graph = defaultdict(list)
	
	#function to add an edge to a graph
	def addEdge(self,u,v):
		self.graph[u].append(v)

	#Function to print a BFS of Graph
	def BFS(self,s):
		
		#Mark all the vertices as not visited 
		visited = [False] * len(self.graph)
		
		#Create a queue for BFS
		queue = []

		#Mark the source node as 
		#visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:
		
			#Dequeue a vertex from
			#queue and print it
			s = queue.pop(0)
			print(s, end=" ")

			#Get all adjacent vertices of the
			#dequeued vertex s. If a adjacent
			#has not been visited, then mark it 
			#visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True

g = Graph()
g.addEdge(0,1)
g.addEdge(0,5)
g.addEdge(1,4)
g.addEdge(2,0)
g.addEdge(2,1)
g.addEdge(3,2)
g.addEdge(5,3)
g.addEdge(3,4)
g.addEdge(4,0)


g.BFS(0)
