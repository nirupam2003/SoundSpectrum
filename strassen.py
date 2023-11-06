from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # For an undirected graph, you may want to add this line.

    def print_adjacency_list(self):
        for node in self.graph:
            neighbors = self.graph[node]
            print(f"Node {node} is connected to: {neighbors}")
    def bfs(self,start_node):
        visited=[]
        queue=[]
        queue.append(start_node)
        visited.append(start_node)
        while queue:
            node=queue.pop(0)
            print(node,end="->")
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.append(neighbour)
    
    def dfs(self,visited,root):
        
        if root not in visited:
            print(root,end="-")
            visited.append(root)
            for neighbor in self.graph[root]:
                self.dfs(visited,neighbor)
# Example usage:
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)

g.print_adjacency_list()
g.bfs(0)

g = Graph()
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.print_adjacency_list()
visited=[]
g.dfs(visited,0)