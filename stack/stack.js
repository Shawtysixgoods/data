class Stack {
  constructor() {
    // Используем массив для хранения элементов
    this.items = [];
  }

  // Добавить элемент на вершину стека
  push(item) {
    this.items.push(item);
  }

  // Удалить и вернуть верхний элемент стека
  pop() {
    return this.items.pop();
  }

  // Получить верхний элемент стека без удаления
  peek() {
    return this.items[this.items.length - 1];
  }

  // Проверка, пуст ли стек
  isEmpty() {
    return this.items.length === 0;
  }
}

// Пример использования
const stack = new Stack();
stack.push("a");
stack.push("b");
console.log(stack.peek()); // b
console.log(stack.pop());  // b
console.log(stack.isEmpty()); // false