class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            print("WARNING: That vertex already exists")
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # Create an empty queue
        q = Queue()
        # Add the starting vertex_id to the queue
        q.enqueue(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first vertex
            v = q.dequeue()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then add all neighbors to the back of the queue
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_vertex)
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first vertex
            v = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if v not in visited:
                # Mark it as visited
                print(v)
                visited.add(v)
                # Then push all neighbors to the top of the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # Check if the node is visited
        # Hint: https://docs.python-guide.org/writing/gotchas/
        # If not...
            # Mark it as visited
            # Print
            # Call DFT_Recursive on each child
        # start with the base case
        if visited is None:
            visited = set()
        # if visited isn't none, add the starting vertex
        visited.add(starting_vertex)
        print(starting_vertex)
        # now the for loop that uses recursion
        # basically, it will loop through beginning with the starting vertex to see if the node has been visited, if it hasn't it will be added to the visited set
        for i in self.vertices[starting_vertex]:
            if i not in visited:
                self.dft_recursive(i, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue
        q = Queue()
        # Add A PATH TO the starting vertex_id to the queue
        q.enqueue([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue, the first PATH
            path = q.dequeue()
            # GRAB THE LAST VERTEX FROM THE PATH
            v = path[-1]
            # CHECK IF IT'S THE TARGET
            if v == destination_vertex:
            # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            if v not in visited:
            # If it has not been visited...
            # Mark it as visited
                visited.add(v)
            # Then add A PATH TO all neighbors to the back of the queue
            # (Make a copy of the path before adding)
                for next_v in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(next_v)
                    q.enqueue(new_path)


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty stack
        s = Stack()
        # Add A PATH TO the starting vertex_id to the stack
        s.push([starting_vertex])
        # Create an empty set to store visited nodes
        visited = set()
        # While the stack is not empty...
        while s.size() > 0:
            # pop, the first PATH
            path = s.pop()
            # GRAB THE LAST VERTEX FROM THE PATH
            v = path[-1]
            # CHECK IF IT'S THE TARGET
            if v == destination_vertex:
             # IF SO, RETURN THE PATH
                return path
            # Check if it's been visited
            if v not in visited:
            # If it has not been visited...
                # Mark it as visited
                visited.add(v)
                # Then add A PATH TO all neighbors to the back of the stack
                    # (Make a copy of the path before adding)
                for next_v in self.get_neighbors(v):
                    new_path = list(path)
                    new_path.append(next_v)
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
​
        This should be done using recursion.
        """
        # start with the base case
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(starting_vertex)
        path = path + [starting_vertex]
        if starting_vertex == destination_vertex:
            return path
        # now the for loop that uses recursion
        # basically, it will loop through beginning with the starting vertex to see if the node has been visited, if it hasn't it will be added to the visited set
        for i in self.vertices[starting_vertex]:
            if i not in visited:
                new_path = self.dfs_recursive(i, destination_vertex, visited, path)
                return new_path
        return None