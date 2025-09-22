// Узел очереди
class QNode {
  constructor(value) {
    // Значение узла
    this.value = value;
    this.next = null;
  }
}

class Queue {
  constructor() {
    // Указатели на голову и хвост очереди
    this.head = null;
    this.tail = null;
    // Размер очереди
    this.size = 0;
  }

  // Добавление элемента в хвост очереди
  enqueue(value) {
    const node = new QNode(value);
    if (!this.tail) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }
    this.size++;
  }

  // Удаление элемента из головы очереди и возврат его
  dequeue() {
    if (!this.head) return undefined;
    const value = this.head.value;
    this.head = this.head.next;
    if (!this.head) this.tail = null;
    this.size--;
    return value;
  }
}

// Пример использования
const queue = new Queue();
queue.enqueue(10);
queue.enqueue(20);
console.log(queue.dequeue()); // 10
console.log(queue.dequeue()); // 20