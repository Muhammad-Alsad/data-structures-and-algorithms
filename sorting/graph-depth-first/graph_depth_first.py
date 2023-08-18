from graph.graph import Graph



def depth_first(self, start_vertex):
            """
            Perform a depth-first traversal of the graph starting from the given vertex.

            Args:
                start_vertex: The vertex to start the traversal from.

            Returns:
                list: A list of vertices in the order of their pre-order depth-first traversal.
            """
            result = []
            visited = set()
            stack = [start_vertex]
            visited.add(start_vertex)

            while len(stack):
                current_vertex = stack.pop()
                result.append(current_vertex.value)
                neighbors = self.get_neighbors(current_vertex)

                for edge in reversed(neighbors):
                    neighbor = edge.vertix
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)

            return result
    

if __name__ == "__main__":
    graph = Graph()
    a = graph.add_vertix('A')
    b = graph.add_vertix('B')
    e = graph.add_vertix('E')
    c = graph.add_vertix('C')
    d = graph.add_vertix('D')
    e = graph.add_vertix('E')
    f = graph.add_vertix('F')
    g = graph.add_vertix('G')
    h = graph.add_vertix('H')

    graph.add_edge(a,b)
    graph.add_edge(a,d)
    
    graph.add_edge(b,d)
    graph.add_edge(b,c)
    
    graph.add_edge(d,e)
    graph.add_edge(d,h)
    graph.add_edge(d,f)
    
    graph.add_edge(f,h)
    graph.add_edge(c,g)

    print(graph.depth_first(a))