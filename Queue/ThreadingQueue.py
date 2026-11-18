import threading
import time
import random

class ThreadSafeQueue:
    def __init__(self):
        self.queue = []
        self.lock = threading.Lock()  # Блокировка для защиты доступа к списку

    def enqueue(self, item):
        with self.lock:  # Захватываем блокировку перед изменением
            self.queue.append(item)

    def dequeue(self):
        with self.lock:
            if len(self.queue) > 0:
                return self.queue.pop(0)
            else:
                print("Очередь пуста!")
                return None

    def peek(self):
        with self.lock:
            if len(self.queue) > 0:
                return self.queue[0]
            else:
                print("Очередь пуста!")
                return None

    def is_empty(self):
        with self.lock:
            return len(self.queue) == 0

    def size(self):
        with self.lock:
            return len(self.queue)


# --- Пример использования с несколькими потоками ---

def producer(q, count):
    """Поток-производитель: добавляет элементы в очередь."""
    for i in range(count):
        item = f"Задача-{i}"
        q.enqueue(item)
        print(f"[Производитель] Добавил: {item}")
        time.sleep(random.uniform(0.1, 0.4))

def consumer(q, name, count):
    """Поток-потребитель: забирает элементы из очереди."""
    for _ in range(count):
        time.sleep(random.uniform(0.2, 0.6))
        item = q.dequeue()
        if item is not None:
            print(f"[{name}] Обработал: {item}")

if __name__ == "__main__":
    ts_queue = ThreadSafeQueue()

    # Создаем потоки
    t_producer = threading.Thread(target=producer, args=(ts_queue, 6))
    t_consumer_1 = threading.Thread(target=consumer, args=(ts_queue, "Потребитель-1", 3))
    t_consumer_2 = threading.Thread(target=consumer, args=(ts_queue, "Потребитель-2", 3))

    # Запускаем потоки
    t_producer.start()
    t_consumer_1.start()
    t_consumer_2.start()

    # Ждем завершения всех потоков
    t_producer.join()
    t_consumer_1.join()
    t_consumer_2.join()

    print(f"Итоговый размер очереди: {ts_queue.size()}")
