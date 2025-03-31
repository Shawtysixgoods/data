
# Односвязаный список
class Node:
    def __init__(self, value):
        """
        Узел, хранящий значение и ссылку на следующий узел.
        """
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        """
        Изначально список пуст, голова (head) = None.
        """
        self.head = None

    def append(self, value):
        """
        Добавление элемента в конец списка.
        """
        new_node = Node(value)
        if not self.head:
            # Если список пуст, новый узел становится головой
            self.head = new_node
            return
        # Иначе идем в конец списка
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, value):
        """
        Добавление элемента в начало списка.
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove(self, value):
        """
        Удаление первого найденного узла со значением 'value'.
        """
        if not self.head:
            print("Список пуст!")
            return
        
        # Если элемент для удаления - это головной узел
        if self.head.value == value:
            self.head = self.head.next
            return
        
        # Поиск узла, который ссылается на узел с удаляемым значением
        current = self.head
        while current.next and current.next.value != value:
            current = current.next
        
        if current.next is None:
            print("Элемент не найден!")
        else:
            # Перепрыгиваем через удаляемый узел
            current.next = current.next.next

    def traverse(self):
        """
        Проход по списку и вывод значений.
        """
        current = self.head
        elements = []
        while current:
            elements.append(current.value)
            current = current.next
        return elements


# Пример использования односвязного списка:
my_list = SinglyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.insert_at_beginning(5)
print(my_list.traverse())  # Вывод: [5, 10, 20]

my_list.remove(10)
print(my_list.traverse())  # Вывод: [5, 20]
