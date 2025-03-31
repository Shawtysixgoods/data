class BSTNode:
    def __init__(self, value):
        """
        Узел двоичного дерева: значение + ссылки на левого и правого потомка.
        """
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        """
        Вставка нового значения в дерево (с сохранением свойств BST).
        """
        if value < self.value:
            # Идем в левое поддерево
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            # Идем в правое поддерево (допустим, равные элементы кладем направо)
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    def search(self, value):
        """
        Поиск значения в дереве.
        """
        if value == self.value:
            return True
        elif value < self.value:
            # Ищем в левом поддереве
            if self.left is None:
                return False
            else:
                return self.left.search(value)
        else:
            # Ищем в правом поддереве
            if self.right is None:
                return False
            else:
                return self.right.search(value)

    def inorder_traversal(self):
        """
        Симметричный обход (in-order traversal): 
        сначала левое поддерево, потом узел, потом правое поддерево.
        """
        elements = []
        # Обходим левое поддерево
        if self.left:
            elements += self.left.inorder_traversal()
        # Добавляем текущее значение
        elements.append(self.value)
        # Обходим правое поддерево
        if self.right:
            elements += self.right.inorder_traversal()
        return elements


# Пример использования BST:
root = BSTNode(10)
root.insert(5)
root.insert(15)
root.insert(2)
root.insert(5)   # вставится справа от узла со значением 5
root.insert(12)
root.insert(20)

print(root.inorder_traversal())  # Вывод: [2, 5, 5, 10, 12, 15, 20]
print(root.search(15))  # Вывод: True
print(root.search(8))   # Вывод: False
