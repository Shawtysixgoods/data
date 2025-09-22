// Узел связанного списка
class Node {
  constructor(value) {
    // Значение узла
    this.value = value;
    // Ссылка на следующий узел
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    // Головной элемент списка
    this.head = null;
  }

  // Добавление нового узла в конец списка
  append(value) {
    const node = new Node(value);
    if (!this.head) {
      this.head = node;
      return;
    }
    let current = this.head;
    while (current.next) {
      current = current.next;
    }
    current.next = node;
  }

  // Вывод значений списка в консоль
  print() {
    let current = this.head;
    while (current) {
      console.log(current.value);
      current = current.next;
    }
  }
}

// Пример использования
const list = new LinkedList();
list.append(1);
list.append(2);
list.append(3);
list.print(); // 1 2 3