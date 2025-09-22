class MinHeap {
  constructor() {
    // Массив для хранения элементов кучи
    this.heap = [];
  }

  // Получение индекса родительского элемента
  parent(i) {
    return Math.floor((i - 1) / 2);
  }

  // Индексы левого и правого детей
  left(i) {
    return 2 * i + 1;
  }

  right(i) {
    return 2 * i + 2;
  }

  // Вставка нового элемента в кучу
  insert(val) {
    this.heap.push(val);
    this.bubbleUp(this.heap.length - 1);
  }

  // Всплытие элемента вверх кучи после вставки
  bubbleUp(index) {
    while (index > 0 && this.heap[this.parent(index)] > this.heap[index]) {
      [this.heap[this.parent(index)], this.heap[index]] = [this.heap[index], this.heap[this.parent(index)]];
      index = this.parent(index);
    }
  }

  // Извлечение минимального элемента (корня)
  extractMin() {
    if (this.heap.length === 0) return undefined;
    if (this.heap.length === 1) return this.heap.pop();
    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.bubbleDown(0);
    return min;
  }

  // Опускание элемента вниз для поддержания свойства кучи
  bubbleDown(index) {
    let left = this.left(index);
    let right = this.right(index);
    let smallest = index;

    if (left < this.heap.length && this.heap[left] < this.heap[smallest]) {
      smallest = left;
    }
    if (right < this.heap.length && this.heap[right] < this.heap[smallest]) {
      smallest = right;
    }
    if (smallest !== index) {
      [this.heap[smallest], this.heap[index]] = [this.heap[index], this.heap[smallest]];
      this.bubbleDown(smallest);
    }
  }
}

// Пример использования
const heap = new MinHeap();
heap.insert(5);
heap.insert(3);
heap.insert(10);
console.log(heap.extractMin()); // 3
console.log(heap.extractMin()); // 5