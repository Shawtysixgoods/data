// Класс для Min Heap
class MinHeap {
  constructor() {
    this.heap = [];
  }

  // Получить индекс родителя
  parentIndex(i) {
    return Math.floor((i - 1) / 2);
  }

  // Получить индекс левого потомка
  leftChildIndex(i) {
    return 2 * i + 1;
  }

  // Получить индекс правого потомка
  rightChildIndex(i) {
    return 2 * i + 2;
  }

  // Поменять два элемента
  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  // Вставить элемент
  insert(value) {
    this.heap.push(value);
    this.siftUp(this.heap.length - 1);
  }

  // Просеивание вверх
  siftUp(index) {
    while (index > 0) {
      const parentIdx = this.parentIndex(index);
      if (this.heap[index] < this.heap[parentIdx]) {
        this.swap(index, parentIdx);
        index = parentIdx;
      } else {
        break;
      }
    }
  }

  // Просеивание вниз
  siftDown(index) {
    while (true) {
      let smallest = index;
      const leftIdx = this.leftChildIndex(index);
      const rightIdx = this.rightChildIndex(index);

      if (leftIdx < this.heap.length && this.heap[leftIdx] < this.heap[smallest]) {
        smallest = leftIdx;
      }

      if (rightIdx < this.heap.length && this.heap[rightIdx] < this.heap[smallest]) {
        smallest = rightIdx;
      }

      if (smallest !== index) {
        this.swap(index, smallest);
        index = smallest;
      } else {
        break;
      }
    }
  }

  // Удалить минимум (корень)
  extractMin() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();

    const min = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.siftDown(0);
    return min;
  }

  // Получить минимум без удаления
  getMin() {
    return this.heap[0];
  }

  // Размер кучи
  size() {
    return this.heap.length;
  }

  // Вывести кучу
  display() {
    console.log(this.heap);
  }
}

// Класс для Max Heap
class MaxHeap {
  constructor() {
    this.heap = [];
  }

  parentIndex(i) {
    return Math.floor((i - 1) / 2);
  }

  leftChildIndex(i) {
    return 2 * i + 1;
  }

  rightChildIndex(i) {
    return 2 * i + 2;
  }

  swap(i, j) {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }

  insert(value) {
    this.heap.push(value);
    this.siftUp(this.heap.length - 1);
  }

  siftUp(index) {
    while (index > 0) {
      const parentIdx = this.parentIndex(index);
      if (this.heap[index] > this.heap[parentIdx]) {
        this.swap(index, parentIdx);
        index = parentIdx;
      } else {
        break;
      }
    }
  }

  siftDown(index) {
    while (true) {
      let largest = index;
      const leftIdx = this.leftChildIndex(index);
      const rightIdx = this.rightChildIndex(index);

      if (leftIdx < this.heap.length && this.heap[leftIdx] > this.heap[largest]) {
        largest = leftIdx;
      }

      if (rightIdx < this.heap.length && this.heap[rightIdx] > this.heap[largest]) {
        largest = rightIdx;
      }

      if (largest !== index) {
        this.swap(index, largest);
        index = largest;
      } else {
        break;
      }
    }
  }

  extractMax() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();

    const max = this.heap[0];
    this.heap[0] = this.heap.pop();
    this.siftDown(0);
    return max;
  }

  getMax() {
    return this.heap[0];
  }

  size() {
    return this.heap.length;
  }

  display() {
    console.log(this.heap);
  }
}

// Пример использования Min Heap
console.log('=== Min Heap ===');
const minHeap = new MinHeap();
minHeap.insert(10);
minHeap.insert(5);
minHeap.insert(20);
minHeap.insert(2);
minHeap.insert(15);

console.log('Min Heap:', minHeap.heap);
console.log('Минимум:', minHeap.getMin());
console.log('Извлечено:', minHeap.extractMin());
console.log('После удаления:', minHeap.heap);

// Пример использования Max Heap
console.log('\n=== Max Heap ===');
const maxHeap = new MaxHeap();
maxHeap.insert(10);
maxHeap.insert(5);
maxHeap.insert(20);
maxHeap.insert(2);
maxHeap.insert(15);

console.log('Max Heap:', maxHeap.heap);
console.log('Максимум:', maxHeap.getMax());
console.log('Извлечено:', maxHeap.extractMax());
console.log('После удаления:', maxHeap.heap);
