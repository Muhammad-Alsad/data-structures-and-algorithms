from graph.graph import (Graph)



def depth_first(self, start_vertex):
        """
        Perform a depth-first traversal of the graph starting from the given vertex.

        Args:
            start_vertex: The vertex to start the traversal from.

        Returns:
            list: A list of vertices in the order of their pre-order depth-first traversal.
        """
        visited = set()
        traversal_result = []

        def dfs(vertex):
            visited.add(vertex)
            traversal_result.append(vertex)

            for neighbor, _ in self.vertices[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)

        dfs(start_vertex)
        return traversal_result
    

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertix('A')
    graph.add_vertix('B')
    graph.add_vertix('C')
    graph.add_vertix('D')
    graph.add_vertix('E')
    graph.add_vertix('F')
    graph.add_vertix('G')
    graph.add_vertix('H')

    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'G')
    graph.add_edge('C', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'H')
    graph.add_edge('D', 'F')

    start_vertex = 'A'
    traversal_result = graph.depth_first(start_vertex)
    print(", ".join(traversal_result))