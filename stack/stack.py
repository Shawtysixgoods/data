class Stack:
    def __init__(self):
        self.stack = []  # Инициализация пустого списка для стека

    def push(self, item):
        # Добавление элемента в стек
        self.stack.append(item)

    def pop(self):
        # Удаление и возврат верхнего элемента стека
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Стек пуст!")

    def peek(self):
        # Возврат верхнего элемента без удаления
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Стек пуст!")

    def is_empty(self):
        # Проверка, пуст ли стек
        return len(self.stack) == 0

    def size(self):
        # Возврат количества элементов в стеке
        return len(self.stack)


# Пример использования стека:
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Вывод: 30 (последний добавленный элемент)
print(stack.peek())  # Вывод: 20 (верхний элемент)
