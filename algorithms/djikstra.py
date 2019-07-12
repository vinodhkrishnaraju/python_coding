# Python program for Dijkstra's single 
# source shortest path algorithm. The program is 
# for adjacency matrix representation of the graph 

# Library for INT_MAX 
import sys 

class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)] 
                    for row in range(vertices)] 

    def printSolution(self, cost): 
        print "Vertex tDistance from Source"
        for node in range(self.V): 
            print node, "t", cost[node] 

    # A utility function to find the vertex with 
    # minimum costance value, from the set of vertices 
    # not yet included in shortest path tree 
    def minDistance(self, cost, visited): 

        # Initilaize minimum costance for next node 
        min = sys.maxint 

        # Search not nearest vertex not in the 
        # shortest path tree 
        for v in range(self.V): 
            if cost[v] < min and visited[v] == False: 
                min = cost[v] 
                min_index = v 

        return min_index 

    # Funtion that implements Dijkstra's single source 
    # shortest path algorithm for a graph represented 
    # using adjacency matrix representation 
    def dijkstra(self, src): 

        cost = [sys.maxint] * self.V 
        cost[src] = 0
        visited = [False] * self.V 

        for cout in range(self.V): 

            # Pick the minimum costance vertex from 
            # the set of vertices not yet processed. 
            # u is always equal to src in first iteration 
            u = self.minDistance(cost, visited) 

            # Put the minimum costance vertex in the 
            # shotest path tree 
            visited[u] = True

            # Update cost value of the adjacent vertices 
            # of the picked vertex only if the current 
            # costance is greater than new costance and 
            # the vertex in not in the shotest path tree 
            for v in range(self.V): 
                new_cost = self.graph[u][v]
                if new_cost > 0 and visited[v] == False and \ 
                cost[v] > cost[u] + new_cost: 
                        cost[v] = cost[u] + new_cost

        self.printSolution(cost) 

# Driver program 
g = Graph(9) 
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 

g.dijkstra(0); 

# This code is contributed by Divyanshu Mehta 
