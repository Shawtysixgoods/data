class PriorityQueue:
    def __init__(self):
        # {priority: [items...]}
        self.queue = {}

    def enqueue(self, item, priority=0):
        # Добавление элемента с указанным приоритетом
        if priority not in self.queue:
            self.queue[priority] = []
        self.queue[priority].append(item)

    def dequeue(self):
        # Удаление и возврат элемента с НАИВЫСШИМ приоритетом
        if self.is_empty():
            print("Очередь пуста!")
            return

        # Находим минимальный приоритет (0, 1, 2, ...)
        min_priority = min(self.queue.keys())
        item = self.queue[min_priority].pop(0)

        # Если список по этому приоритету опустел — удаляем ключ
        if len(self.queue[min_priority]) == 0:
            del self.queue[min_priority]

        return item

    def peek(self):
        # Просмотр первого элемента с наивысшим приоритетом без удаления
        if self.is_empty():
            print("Очередь пуста!")
            return

        min_priority = min(self.queue.keys())
        return self.queue[min_priority][0]

    def is_empty(self):
        # Пустая, если в словаре нет ключей
        return len(self.queue) == 0

    def size(self):
        # Общее количество элементов по всем приоритетам
        return sum(len(items) for items in self.queue.values())


# Пример использования очереди с приоритетом:
pq = PriorityQueue()
pq.enqueue(10, priority=2)
pq.enqueue(20, priority=1)
pq.enqueue(30, priority=3)
pq.enqueue(40, priority=1)

print(pq.dequeue())  # 20 (приоритет 1)
print(pq.peek())     # 40 (следующий с приоритетом 1)
