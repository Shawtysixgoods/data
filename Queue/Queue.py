class Queue:
    def __init__(self):
        self.queue = []  # Инициализация пустого списка для очереди

    def enqueue(self, item):
        # Добавление элемента в конец очереди
        self.queue.append(item)

    def dequeue(self):
        # Удаление и возврат первого элемента очереди
        if not self.is_empty():
            return self.queue.pop(0)  # Извлечение элемента с начала
        else:
            print("Очередь пуста!")

    def peek(self):
        # Возврат первого элемента без удаления
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Очередь пуста!")

    def is_empty(self):
        # Проверка, пуста ли очередь
        return len(self.queue) == 0

    def size(self):
        # Возврат количества элементов в очереди
        return len(self.queue)


# Пример использования очереди:
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())  # Вывод: 10 (первый добавленный элемент)
print(queue.peek())  # Вывод: 20 (первый элемент)
