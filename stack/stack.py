class Stack:
    def __init__(self):
        # Инициализируем пустой список для хранения элементов стека
        self.stack = []

    def push(self, item):
        # Добавление элемента на вершину стека
        self.stack.append(item)

    def pop(self):
        # Удаление элемента с вершины стека
        if not self.is_empty():
            return self.stack.pop()
        return "Стек пуст"

    def peek(self):
        # Получение элемента на вершине стека без его удаления
        if not self.is_empty():
            return self.stack[-1]
        return "Стек пуст"

    def is_empty(self):
        # Проверка, пуст ли стек
        return len(self.stack) == 0

# Пример использования
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack.pop())  # 3
print(stack.peek())  # 2
