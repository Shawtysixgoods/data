from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    # Вставить значение
    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)
    
    # Поиск значения
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        
        if value == node.value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    # Средний обход (Inorder)
    def inorder_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.value)
            self.inorder_traversal(node.right, result)
        
        return result
    
    # Прямой обход (Preorder)
    def preorder_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            result.append(node.value)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        
        return result
    
    # Обратный обход (Postorder)
    def postorder_traversal(self, node=None, result=None):
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.value)
        
        return result
    
    # Обход в ширину (Level-order)
    def level_order_traversal(self):
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            node = queue.popleft()
            result.append(node.value)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
    
    # Найти минимальное значение
    def find_min(self, node=None):
        if node is None:
            node = self.root
        
        while node.left:
            node = node.left
        
        return node.value
    
    # Найти максимальное значение
    def find_max(self, node=None):
        if node is None:
            node = self.root
        
        while node.right:
            node = node.right
        
        return node.value

# Пример использования
if __name__ == "__main__":
    bst = BinarySearchTree()
    
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    
    print('Средний обход (Inorder):', bst.inorder_traversal())
    print('Прямой обход (Preorder):', bst.preorder_traversal())
    print('Обратный обход (Postorder):', bst.postorder_traversal())
    print('Обход в ширину (Level-order):', bst.level_order_traversal())
    
    print('Поиск 40:', bst.search(40))  # True
    print('Поиск 100:', bst.search(100))  # False
    
    print('Минимум:', bst.find_min())  # 20
    print('Максимум:', bst.find_max())  # 80
