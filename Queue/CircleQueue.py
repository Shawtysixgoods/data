class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity  # Фиксированный размер очереди
        self.queue = [None] * capacity  # Массив фиксированного размера
        self.front = -1  # Указатель на начало очереди
        self.rear = -1   # Указатель на конец очереди

    def enqueue(self, item):
        # Проверка переполнения: следующая позиция rear совпадает с front
        if (self.rear + 1) % self.capacity == self.front:
            print("Очередь переполнена!")
            return
        
        # Если очередь пустая, инициализируем front
        if self.front == -1:
            self.front = 0
        
        # Циклически увеличиваем rear и добавляем элемент
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            print("Очередь пуста!")
            return None
        
        # Сохраняем элемент для возврата
        item = self.queue[self.front]
        
        # Если это был последний элемент, сбрасываем очередь
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Циклически увеличиваем front
            self.front = (self.front + 1) % self.capacity
        
        return item

    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            print("Очередь пуста!")
            return None

    def is_empty(self):
        return self.front == -1

    def size(self):
        if self.is_empty():
            return 0
        # Вычисляем размер с учетом циклической структуры
        if self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.capacity - self.front + self.rear + 1


# Пример использования:
queue = CircularQueue(5)  # Создаем очередь размером 5
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # Вывод: 10
print(queue.peek())     # Вывод: 20
print(queue.size())     # Вывод: 2

# Заполняем очередь полностью
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)  # Вывод: Очередь переполнена!
