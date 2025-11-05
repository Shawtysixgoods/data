class MinHeap:
    def __init__(self):
        self.heap = []
    
    def parent_index(self, i):
        return (i - 1) // 2
    
    def left_child_index(self, i):
        return 2 * i + 1
    
    def right_child_index(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    # Вставить элемент
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)
    
    # Просеивание вверх
    def sift_up(self, index):
        while index > 0:
            parent_idx = self.parent_index(index)
            if self.heap[index] < self.heap[parent_idx]:
                self.swap(index, parent_idx)
                index = parent_idx
            else:
                break
    
    # Просеивание вниз
    def sift_down(self, index):
        while True:
            smallest = index
            left_idx = self.left_child_index(index)
            right_idx = self.right_child_index(index)
            
            if left_idx < len(self.heap) and self.heap[left_idx] < self.heap[smallest]:
                smallest = left_idx
            
            if right_idx < len(self.heap) and self.heap[right_idx] < self.heap[smallest]:
                smallest = right_idx
            
            if smallest != index:
                self.swap(index, smallest)
                index = smallest
            else:
                break
    
    # Удалить минимум
    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return min_val
    
    # Получить минимум
    def get_min(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)
    
    def display(self):
        print(self.heap)


class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent_index(self, i):
        return (i - 1) // 2
    
    def left_child_index(self, i):
        return 2 * i + 1
    
    def right_child_index(self, i):
        return 2 * i + 2
    
    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    # Вставить элемент
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)
    
    # Просеивание вверх
    def sift_up(self, index):
        while index > 0:
            parent_idx = self.parent_index(index)
            if self.heap[index] > self.heap[parent_idx]:
                self.swap(index, parent_idx)
                index = parent_idx
            else:
                break
    
    # Просеивание вниз
    def sift_down(self, index):
        while True:
            largest = index
            left_idx = self.left_child_index(index)
            right_idx = self.right_child_index(index)
            
            if left_idx < len(self.heap) and self.heap[left_idx] > self.heap[largest]:
                largest = left_idx
            
            if right_idx < len(self.heap) and self.heap[right_idx] > self.heap[largest]:
                largest = right_idx
            
            if largest != index:
                self.swap(index, largest)
                index = largest
            else:
                break
    
    # Удалить максимум
    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return max_val
    
    # Получить максимум
    def get_max(self):
        return self.heap[0] if self.heap else None
    
    def size(self):
        return len(self.heap)
    
    def display(self):
        print(self.heap)


# Пример использования Min Heap
if __name__ == "__main__":
    print("=== Min Heap ===")
    min_heap = MinHeap()
    min_heap.insert(10)
    min_heap.insert(5)
    min_heap.insert(20)
    min_heap.insert(2)
    min_heap.insert(15)
    
    print("Min Heap:", end=" ")
    min_heap.display()
    print("Минимум:", min_heap.get_min())
    print("Извлечено:", min_heap.extract_min())
    print("После удаления:", end=" ")
    min_heap.display()
    
    # Пример использования Max Heap
    print("\n=== Max Heap ===")
    max_heap = MaxHeap()
    max_heap.insert(10)
    max_heap.insert(5)
    max_heap.insert(20)
    max_heap.insert(2)
    max_heap.insert(15)
    
    print("Max Heap:", end=" ")
    max_heap.display()
    print("Максимум:", max_heap.get_max())
    print("Извлечено:", max_heap.extract_max())
    print("После удаления:", end=" ")
    max_heap.display()
