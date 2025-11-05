class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    # Простая хеш-функция
    def hash(self, key):
        hash_value = 0
        
        if isinstance(key, str):
            for char in key:
                hash_value += ord(char)
        else:
            hash_value = hash(key)
        
        return hash_value % self.size
    
    # Вставить элемент
    def insert(self, key, value):
        index = self.hash(key)
        
        # Проверяем, существует ли уже такой ключ
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)  # Обновляем значение
                return
        
        # Добавляем новую пару ключ-значение
        self.table[index].append((key, value))
    
    # Поиск значения по ключу
    def search(self, key):
        index = self.hash(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        return None
    
    # Удалить элемент
    def delete(self, key):
        index = self.hash(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                return True
        
        return False
    
    # Вывести таблицу
    def display(self):
        for i in range(self.size):
            if self.table[i]:
                print(f"Индекс {i}:", self.table[i])
    
    # Получить все ключи
    def keys(self):
        all_keys = []
        
        for bucket in self.table:
            for k, v in bucket:
                all_keys.append(k)
        
        return all_keys
    
    # Получить все значения
    def values(self):
        all_values = []
        
        for bucket in self.table:
            for k, v in bucket:
                all_values.append(v)
        
        return all_values
    
    # Получить все пары ключ-значение
    def items(self):
        all_items = []
        
        for bucket in self.table:
            for k, v in bucket:
                all_items.append((k, v))
        
        return all_items


# Пример использования
if __name__ == "__main__":
    hash_table = HashTable(5)
    
    hash_table.insert('name', 'John')
    hash_table.insert('age', 30)
    hash_table.insert('city', 'New York')
    hash_table.insert('profession', 'Developer')
    hash_table.insert('hobby', 'Gaming')
    
    print("Хеш-таблица:")
    hash_table.display()
    
    print("\nПоиск:")
    print('name:', hash_table.search('name'))
    print('age:', hash_table.search('age'))
    print('email:', hash_table.search('email'))  # None
    
    print("\nВсе ключи:", hash_table.keys())
    print("Все значения:", hash_table.values())
    print("Все пары:", hash_table.items())
    
    print("\nУдаление 'city':")
    hash_table.delete('city')
    hash_table.display()
    
    print("\nОбновление 'age':")
    hash_table.insert('age', 31)
    hash_table.display()
