class MyArray {
  constructor() {
    // Длина массива
    this.length = 0;
    // Объект для хранения элементов по индексам
    this.data = {};
  }

  // Получение элемента по индексу
  get(index) {
    return this.data[index];
  }

  // Добавление элемента в конец массива
  push(item) {
    this.data[this.length] = item;
    this.length++;
  }

  // Удаление последнего элемента и возврат его
  pop() {
    if (this.length === 0) return undefined;
    const last = this.data[this.length - 1];
    delete this.data[this.length - 1];
    this.length--;
    return last;
  }

  // Вставка элемента в указанную позицию сдвигая элементы вправо
  insertAt(item, index) {
    if (index > this.length) return;
    for (let i = this.length; i > index; i--) {
      this.data[i] = this.data[i - 1];
    }
    this.data[index] = item;
    this.length++;
  }

  // Удаление элемента по индексу + сдвиг элементов влево
  deleteAt(index) {
    if (index >= this.length) return;
    for (let i = index; i < this.length - 1; i++) {
      this.data[i] = this.data[i + 1];
    }
    delete this.data[this.length - 1];
    this.length--;
  }
}

// Пример использования
const arr = new MyArray();
arr.push(10);
arr.push(20);
arr.push(30);
console.log(arr.get(1)); // 20
arr.insertAt(15, 1);
console.log(arr.get(1)); // 15
arr.deleteAt(2);
console.log(arr.get(2)); // 30
console.log(arr.pop()); // 30