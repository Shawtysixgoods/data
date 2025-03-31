class Graph:
    def __init__(self):
        """
        Словарь, где ключ – вершина, а значение – список смежных вершин.
        """
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        """
        Добавить вершину в граф, если такой вершины ещё нет.
        """
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

    def add_edge(self, v1, v2):
        """
        Добавить ребро между вершинами v1 и v2.
        Предположим, что у нас неориентированный граф.
        """
        if v1 in self.adjacency_list and v2 in self.adjacency_list:
            self.adjacency_list[v1].append(v2)
            self.adjacency_list[v2].append(v1)
        else:
            print("Одна или обе вершины отсутствуют!")

    def get_vertices(self):
        """
        Получить все вершины графа.
        """
        return list(self.adjacency_list.keys())

    def get_edges(self):
        """
        Получить все рёбра в виде списка кортежей (v1, v2).
        Для неориентированного графа нужно аккуратно исключать дубликаты.
        """
        edges = []
        visited = set()  # Чтобы не дублировать (v1, v2) и (v2, v1)
        for v1 in self.adjacency_list:
            for v2 in self.adjacency_list[v1]:
                if (v2, v1) not in visited:
                    edges.append((v1, v2))
                    visited.add((v1, v2))
        return edges

    def show_graph(self):
        """
        Простой вывод графа в консоль.
        """
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])


# Пример использования графа:
g = Graph()
g.add_vertex("A")
g.add_vertex("B")
g.add_vertex("C")
g.add_edge("A", "B")
g.add_edge("B", "C")

g.show_graph()
# Вывод:
# A : ['B']
# B : ['A', 'C']
# C : ['B']

print("Vertices:", g.get_vertices())  
# Вывод: ['A', 'B', 'C']

print("Edges:", g.get_edges())        
# Вывод: [('A', 'B'), ('B', 'C')]
