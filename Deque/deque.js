class Deque {
  constructor() {
    // Объект для хранения элементов
    this.items = {};
    // Индексы для "переднего" и "заднего" концов дека
    this.frontIndex = 0;
    this.backIndex = -1;
  }

  // Добавление элемента в начало дека
  pushFront(item) {
    this.frontIndex--;
    this.items[this.frontIndex] = item;
  }

  // Добавление элемента в конец дека
  pushBack(item) {
    this.backIndex++;
    this.items[this.backIndex] = item;
  }

  // Удаление и возврат элемента из начала дека
  popFront() {
    if (this.isEmpty()) return undefined;
    const item = this.items[this.frontIndex];
    delete this.items[this.frontIndex];
    this.frontIndex++;
    return item;
  }

  // Удаление и возврат элемента из конца дека
  popBack() {
    if (this.isEmpty()) return undefined;
    const item = this.items[this.backIndex];
    delete this.items[this.backIndex];
    this.backIndex--;
    return item;
  }

  // Проверка, пуст ли дек
  isEmpty() {
    return this.backIndex < this.frontIndex;
  }
}

// Пример использования
const deque = new Deque();
deque.pushBack(1);
deque.pushBack(2);
deque.pushFront(0);
console.log(deque.popFront()); // 0
console.log(deque.popBack());  // 2