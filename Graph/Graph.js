// Класс для представления графа через список смежности
class Graph {
  constructor() {
    this.adjacencyList = new Map();
  }

  // Добавить вершину
  addVertex(vertex) {
    if (!this.adjacencyList.has(vertex)) {
      this.adjacencyList.set(vertex, []);
    }
  }

  // Добавить неориентированное ребро (двусторонне)
  addEdge(vertex1, vertex2, weight = 1) {
    this.addVertex(vertex1);
    this.addVertex(vertex2);
    
    this.adjacencyList.get(vertex1).push({ node: vertex2, weight });
    this.adjacencyList.get(vertex2).push({ node: vertex1, weight });
  }

  // Добавить ориентированное ребро (односторонне)
  addDirectedEdge(from, to, weight = 1) {
    this.addVertex(from);
    this.addVertex(to);
    
    this.adjacencyList.get(from).push({ node: to, weight });
  }

  // Получить соседей вершины
  getNeighbors(vertex) {
    return this.adjacencyList.get(vertex) || [];
  }

  // Поиск в глубину (DFS)
  dfs(startVertex, visited = new Set()) {
    console.log(startVertex);
    visited.add(startVertex);

    for (const neighbor of this.getNeighbors(startVertex)) {
      if (!visited.has(neighbor.node)) {
        this.dfs(neighbor.node, visited);
      }
    }
  }

  // Поиск в ширину (BFS)
  bfs(startVertex) {
    const visited = new Set();
    const queue = [startVertex];
    visited.add(startVertex);

    while (queue.length > 0) {
      const vertex = queue.shift();
      console.log(vertex);

      for (const neighbor of this.getNeighbors(vertex)) {
        if (!visited.has(neighbor.node)) {
          visited.add(neighbor.node);
          queue.push(neighbor.node);
        }
      }
    }
  }

  // Вывести граф
  display() {
    for (const [vertex, edges] of this.adjacencyList) {
      console.log(`${vertex} ->`, edges.map(e => `${e.node}(${e.weight})`).join(', '));
    }
  }
}

// Пример использования
const graph = new Graph();

graph.addEdge('A', 'B', 5);
graph.addEdge('A', 'C', 3);
graph.addEdge('B', 'D', 2);
graph.addEdge('C', 'D', 1);
graph.addEdge('D', 'E', 4);

console.log('Граф:');
graph.display();

console.log('\nПоиск в глубину (DFS) с вершины A:');
graph.dfs('A');

console.log('\nПоиск в ширину (BFS) с вершины A:');
graph.bfs('A');
