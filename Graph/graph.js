class Graph {
  constructor() {
    // Словарь смежности: ключ - вершина, значение - массив соседей
    this.adjacencyList = {};
  }

  // Добавление вершины в граф
  addVertex(vertex) {
    if (!this.adjacencyList[vertex]) this.adjacencyList[vertex] = [];
  }

  // Добавление ребра между двумя вершинами (неориентированный граф)
  addEdge(v1, v2) {
    this.adjacencyList[v1].push(v2);
    this.adjacencyList[v2].push(v1);
  }

  // Получение всех соседей вершины
  getNeighbors(vertex) {
    return this.adjacencyList[vertex];
  }
}

// Пример использования
const graph = new Graph();
graph.addVertex("A");
graph.addVertex("B");
graph.addEdge("A", "B");
console.log(graph.getNeighbors("A")); // ["B"]
console.log(graph.getNeighbors("B")); // ["A"]