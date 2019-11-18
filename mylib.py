

#                   ----------------------------------------------------------------------
#                   |             * PLATONOV Sergey         KALTRACHIAN Téo              |
#                   |             * Algorithmes avancées                                 |
#                   |             * Algorithme de Ford-Fulkerson                         | 
#                   |             * HEPIA ITI sem. 3            * mylib.py               | 
#                   ----------------------------------------------------------------------


#============================================================#
#                         Imports                            #
#============================================================#
from collections import defaultdict 
import sys

#============================================================#
#                   Terminal Color Class                     #
#============================================================#
class bcolors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#============================================================#
#                   Null Matrix Generation                   #
#============================================================#
def generate_matrix_of_dimension(width, height):
    zero_line = []
    zMatrix = []
    for i in range(height):
        zero_line = []
        for j in range(width):
            zero_line.append(0)
        zMatrix.append(zero_line)
    return zMatrix

#============================================================#
#          Graph Class - with corresponding methods          #
#============================================================#
# Organizes all the edge capacities, and allows operations 
class Graph: 
    def __init__(self, graph): 
        # residual graph 
        self.graph = graph 
        self. ROW = len(graph) 
   
    # Returns true if there is a path from source 's' to sink 't' in 
    # residual graph. Also fills parent[] to store path
    def BFS(self,s, t, parent): 
  
        # Mark all the vertices as not visited 
        visited = [False]*(self.ROW) 
          
        # Create a queue for BFS 
        queue = [] 
          
        # Mark the source node as visited and enqueue it 
        queue.append(s) 
        visited[s] = True
           
         # Standard BFS Loop 
        while queue: 
  
            # Dequeue a vertex from queue and print it 
            u = queue.pop(0) 
          
            # Get all adjacent vertices of the dequeued vertex u 
            # If a adjacent has not been visited, then mark it 
            # visited and enqueue it 
            for ind, val in enumerate(self.graph[u]): 
                if visited[ind] == False and val > 0 : 
                    queue.append(ind) 
                    visited[ind] = True
                    parent[ind] = u 
  
        # If we reached sink in BFS starting from source, then return 
        # true, else false 
        return True if visited[t] else False
              
      
    # Returns tne maximum flow from s to t in the given graph 
    def FordFulkerson(self, source, sink): 
  
        # This array is filled by BFS and to store path 
        parent = [-1]*(self.ROW) 
  
        max_flow = 0 # There is no flow initially 
  
        # Augment the flow while there is path from source to sink 
        while self.BFS(source, sink, parent) : 
  
            # Find minimum residual capacity of the edges along the 
            # path filled by BFS. Or we can say find the maximum flow 
            # through the path found. 
            path_flow = float("Inf") 
            s = sink 
            while(s !=  source): 
                path_flow = min(path_flow, self.graph[parent[s]][s]) 
                s = parent[s] 
  
            # Add path flow to overall flow 
            max_flow +=  path_flow 
  
            # update residual capacities of the edges and reverse edges 
            # along the path 
            v = sink 
            while(v !=  source): 
                u = parent[v] 
                self.graph[u][v] -= path_flow 
                self.graph[v][u] += path_flow 
                v = parent[v] 


<<<<<<< HEAD
        for i in range(sink):
            print(str(self.graph[i]))
            
        return Graph.graph 
=======
        # for i in range(sink + 1):
        #     print(str(self.graph[i]))
        new_graph = self.graph
        return (max_flow, new_graph) 
>>>>>>> 4676b7581222f714b52c204c8f001bb7e06a8435
