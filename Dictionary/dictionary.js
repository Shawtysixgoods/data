class Dictionary {
  constructor() {
    // Используем встроенный Map для хранения ключей и значений
    this.items = new Map();
  }

  // Добавление пары ключ-значение
  set(key, value) {
    this.items.set(key, value);
  }

  // Получение значения по ключу
  get(key) {
    return this.items.get(key);
  }

  // Проверка наличия ключа
  has(key) {
    return this.items.has(key);
  }

  // Удаление пары по ключу
  delete(key) {
    return this.items.delete(key);
  }

  // Получить все ключи в массиве
  keys() {
    return Array.from(this.items.keys());
  }
}

// Пример использования
const dict = new Dictionary();
dict.set("name", "Alice");
dict.set("age", 25);
console.log(dict.get("name")); // Alice
console.log(dict.has("age"));  // true
dict.delete("age");
console.log(dict.keys());      // ["name"]