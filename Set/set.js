class MySet {
  constructor() {
    // Объект для хранения уникальных значений
    this.items = {};
  }

  // Добавление значения, если его нет
  add(value) {
    this.items[value] = true;
  }

  // Проверка наличия значения
  has(value) {
    return this.items.hasOwnProperty(value);
  }

  // Удаление значения
  delete(value) {
    if (this.has(value)) {
      delete this.items[value];
      return true;
    }
    return false;
  }

  // Получение всех значений множества
  values() {
    return Object.keys(this.items);
  }
}

// Пример использования
const set = new MySet();
set.add(1);
set.add(2);
console.log(set.has(1)); // true
set.delete(1);
console.log(set.values()); // ["2"]