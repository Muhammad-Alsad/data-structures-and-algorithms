from collections import deque 

class Queue:
    """
        A simple implementation of a queue using a deque.
    """

    def __init__(self):
        """
                Initializes an empty queue.
        """
        self.dq = deque()

    def enqueue(self, value):
        """
                    Adds a value to the back (end) of the queue.

        Args:
            value: The value to be added to the queue.
        """
        self.dq.append(value)

    def dequeue(self):
        """
                    Removes and returns the front (leftmost) value from the queue.

        Returns:
            The front value of the queue.

            """
        return self.dq.popleft()

    def __len__(self):
        """
                    Returns the number of elements in the queue.

        Returns:
            The number of elements in the queue.
        """
        return len(self.dq)

class Vertix:
    """
              Represents a vertex in a graph.

    Attributes:
        value: The value associated with the vertex.  
    """

    def __init__(self, value):
        """
        Initializes a new vertex with the given value.

        Args:
            value: The value associated with the vertex.
        """

        self.value = value

    def __str__(self):
        """
        Returns a string representation of the vertex's value.

        Returns:
            A string representation of the vertex's value.
        """
        return self.value

class Edge:
    """
    Represents an edge in a graph.

    Attributes:
        vertex: The vertex connected by this edge.
        weight: The weight of the edge (default is 0).
    """
    def __init__(self, vertix, weight=0):
        """
        Initializes a new edge connecting the given vertex with an optional weight.

        Args:
            vertex: The vertex connected by this edge.
            weight: The weight of the edge (default is 0).
        """
        self.weight = weight
        self.vertix = vertix

class Graph:
    """
    Represents a graph data structure.

    Attributes:
        __adj_list (dict): A dictionary representing the adjacency list of the graph.
    """    

    def __init__(self):
        """
        Initializes an empty graph with an empty adjacency list.
        """        

        self.__adj_list = {}
      
    def add_vertix(self,value):
      """
        Adds a vertex to the graph with the given value.

        Args:
            value: The value associated with the new vertex.

        Returns:
            The newly created vertex.
      """      

      vertix = Vertix(value)
      self.__adj_list[vertix] = []
      return vertix

    def add_edge(self, start_vertix, end_vertix, weight=0):
        """
        Adds an edge between two vertices in the graph.

        Args:
            start_vertex: The starting vertex of the edge.
            end_vertex: The ending vertex of the edge.
            weight: The weight of the edge (default is 0).
        """        
        if start_vertix not in self.__adj_list:
            raise KeyError("Start vertex is not found")
        if end_vertix not in self.__adj_list:
            raise KeyError("End vertex is not found")
        edge1 = Edge(end_vertix, weight)
        edge2 = Edge(start_vertix, weight)
        self.__adj_list[start_vertix].append(edge1)
        self.__adj_list[end_vertix].append(edge2)

  
  
    def get_vertices(self):
      """
        Returns a list of all vertices in the graph.

        Returns:
            A list of all vertices in the graph.
        """      
      return self.__adj_list.keys()

  
    def size(self):
      """
        Returns the number of vertices in the graph.

        Returns:
            The number of vertices in the graph.
        """     
      return len(self.__adj_list)
  
    def get_neighbors(self,vertix):
      """
        Returns a list of neighbors for the given vertex.

        Args:
            vertex: The vertex to find neighbors for.

        Returns:
            A list of neighbor vertices.
        """      
      return self.__adj_list.get(vertix, [])
  
    def breadth_first(self,start_vertix):
        """
        Performs a breadth-first traversal of the graph starting from the specified vertex.

        Args:
            start_vertex: The vertex to start the traversal from.

        Returns:
            A list containing the vertices visited during the breadth-first traversal.
        """        
    
        result = []
        visted = set()
        q = Queue()

        q.enqueue(start_vertix)
        visted.add(start_vertix)

        while len(q):
            current_vertix = q.dequeue()

            result.append(current_vertix.value)

            neighbors =self.get_neighbors(current_vertix)

            for edge in neighbors:
                neighbor = edge.vertix
                if neighbor not in visted:
                    q.enqueue(neighbor)
                    visted.add(neighbor)

        return result

def business_trip(graph, cities):
    """
         
    Calculate the cost of a business trip between cities using direct flights.

    This function determines whether a trip is possible with direct flights
    between the provided cities and calculates the total cost of the trip.
    """
    start_city = cities.pop(0)
    vertixes  = graph.get_vertices()
    start_vertix = None
    
    for vertex in vertixes:
        if vertex.value == start_city:
            start_vertix = vertex
    
    total_cost = 0
    current_vertix = start_vertix

    while cities:
        next_city = cities.pop(0)
        neighbors = graph.get_neighbors(current_vertix)
        check = False

        for neighbor in neighbors:
            
            if neighbor.vertix.value == next_city:
                check = True
                total_cost += neighbor.weight
                current_vertix = neighbor.vertix

        if not check:
            return None
        # if next_city != current_vertix.value:
        #     return "False"
    

    return total_cost  

    


 


if __name__ == "__main__":
    pass
    # g = Graph()
    # a = g.add_vertix('A')
    # b = g.add_vertix('B')
    # e = g.add_vertix('E')
    # c = g.add_vertix('C')
    # d = g.add_vertix('D')

    # g.add_edge(a,b)
    # g.add_edge(a,c)
    # g.add_edge(b,d)
    # g.add_edge(b,e)
    # g.add_edge(e,d)
    # g.add_edge(e,c)
    # print(g.breadth_first(a))



    
