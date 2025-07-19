# Title  : Create an undirected graph using dict
# Author : Kiran raj R.
# Date   : 19/07/2025

class Graph:
    def __init__(self, directed=False):
        # adj will map each node to a list of its neighbors
        # each key is a node, and the value is a list of neighbors.
        self.adj = {}           
        self.directed = directed  # whether edges are one‑way

    def add_node(self, u):
        # Checks if u exists in adj; if not, creates an empty list for its neighbors.
        if u not in self.adj:
            self.adj[u] = []

    def add_edge(self, u, v):
        # Check both nodes exist in the graph
        self.add_node(u)
        self.add_node(v)

        # Add the edge u → v
        self.adj[u].append(v)

        # If undirected, also add v → u
        if not self.directed:
            self.adj[v].append(u)

    def __repr__(self):
        # Return each node and its neighbors
        result = []
        for node, neighbors in self.adj.items():
            result.append(f"{node}: {neighbors}")
        return "\n".join(result)

if __name__ == "__main__":
    # Create an undirected graph
    g = Graph(directed=False)

    g.add_edge(0, 1)   
    g.add_edge(0, 2)   
    g.add_edge(1, 3)   
    g.add_edge(2, 4)  
    g.add_edge(4, 5)

    print(g)