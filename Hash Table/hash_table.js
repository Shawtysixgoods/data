// Простая реализация хеш-таблицы методом цепочек (Chaining)
class HashTable {
  constructor(size = 10) {
    this.size = size;
    this.table = new Array(size);
    
    // Инициализируем каждый индекс пустым массивом
    for (let i = 0; i < size; i++) {
      this.table[i] = [];
    }
  }

  // Простая хеш-функция
  hash(key) {
    let hashValue = 0;
    
    for (let i = 0; i < key.length; i++) {
      hashValue += key.charCodeAt(i);
    }
    
    return hashValue % this.size;
  }

  // Вставить элемент
  insert(key, value) {
    const index = this.hash(key);
    
    // Проверяем, существует ли уже такой ключ
    for (let i = 0; i < this.table[index].length; i++) {
      if (this.table[index][i][0] === key) {
        this.table[index][i][1] = value; // Обновляем значение
        return;
      }
    }
    
    // Добавляем новую пару ключ-значение
    this.table[index].push([key, value]);
  }

  // Поиск значения по ключу
  search(key) {
    const index = this.hash(key);
    
    for (let i = 0; i < this.table[index].length; i++) {
      if (this.table[index][i][0] === key) {
        return this.table[index][i][1];
      }
    }
    
    return undefined;
  }

  // Удалить элемент
  delete(key) {
    const index = this.hash(key);
    
    for (let i = 0; i < this.table[index].length; i++) {
      if (this.table[index][i][0] === key) {
        this.table[index].splice(i, 1);
        return true;
      }
    }
    
    return false;
  }

  // Вывести таблицу
  display() {
    for (let i = 0; i < this.size; i++) {
      if (this.table[i].length > 0) {
        console.log(`Индекс ${i}:`, this.table[i]);
      }
    }
  }

  // Получить все ключи
  keys() {
    const allKeys = [];
    
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.table[i].length; j++) {
        allKeys.push(this.table[i][j][0]);
      }
    }
    
    return allKeys;
  }

  // Получить все значения
  values() {
    const allValues = [];
    
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.table[i].length; j++) {
        allValues.push(this.table[i][j][1]);
      }
    }
    
    return allValues;
  }
}

// Пример использования
const hashTable = new HashTable(5);

hashTable.insert('name', 'John');
hashTable.insert('age', 30);
hashTable.insert('city', 'New York');
hashTable.insert('profession', 'Developer');
hashTable.insert('hobby', 'Gaming');

console.log('Хеш-таблица:');
hashTable.display();

console.log('\nПоиск:');
console.log('name:', hashTable.search('name'));
console.log('age:', hashTable.search('age'));
console.log('email:', hashTable.search('email')); // undefined

console.log('\nВсе ключи:', hashTable.keys());
console.log('Все значения:', hashTable.values());

console.log('\nУдаление "city":');
hashTable.delete('city');
hashTable.display();

console.log('\nОбновление "age":');
hashTable.insert('age', 31);
hashTable.display();
