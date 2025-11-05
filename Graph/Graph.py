from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.adjacency_list = defaultdict(list)
    
    # Добавить вершину
    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    # Добавить неориентированное ребро
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        self.adjacency_list[vertex1].append({'node': vertex2, 'weight': weight})
        self.adjacency_list[vertex2].append({'node': vertex1, 'weight': weight})
    
    # Добавить ориентированное ребро
    def add_directed_edge(self, from_vertex, to_vertex, weight=1):
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        self.adjacency_list[from_vertex].append({'node': to_vertex, 'weight': weight})
    
    # Получить соседей вершины
    def get_neighbors(self, vertex):
        return self.adjacency_list.get(vertex, [])
    
    # Поиск в глубину (DFS) - рекурсивный
    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()
        
        print(start_vertex, end=' ')
        visited.add(start_vertex)
        
        for neighbor in self.get_neighbors(start_vertex):
            if neighbor['node'] not in visited:
                self.dfs(neighbor['node'], visited)
    
    # Поиск в ширину (BFS)
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)
        
        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            
            for neighbor in self.get_neighbors(vertex):
                if neighbor['node'] not in visited:
                    visited.add(neighbor['node'])
                    queue.append(neighbor['node'])
    
    # Вывести граф
    def display(self):
        for vertex in self.adjacency_list:
            neighbors = self.adjacency_list[vertex]
            edges_str = ', '.join([f"{n['node']}({n['weight']})" for n in neighbors])
            print(f"{vertex} -> {edges_str}")

# Пример использования
if __name__ == "__main__":
    graph = Graph()
    
    graph.add_edge('A', 'B', 5)
    graph.add_edge('A', 'C', 3)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('C', 'D', 1)
    graph.add_edge('D', 'E', 4)
    
    print("Граф:")
    graph.display()
    
    print("\nПоиск в глубину (DFS) с вершины A:")
    graph.dfs('A')
    
    print("\n\nПоиск в ширину (BFS) с вершины A:")
    graph.bfs('A')
