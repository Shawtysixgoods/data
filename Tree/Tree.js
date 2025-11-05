// Класс для узла бинарного дерева
class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

// Класс для бинарного дерева поиска
class BinarySearchTree {
  constructor() {
    this.root = null;
  }

  // Вставить значение
  insert(value) {
    const newNode = new TreeNode(value);
    
    if (this.root === null) {
      this.root = newNode;
      return this;
    }
    
    let current = this.root;
    while (true) {
      if (value === current.value) return undefined; // Дубликаты не допускаются
      
      if (value < current.value) {
        if (current.left === null) {
          current.left = newNode;
          return this;
        }
        current = current.left;
      } else {
        if (current.right === null) {
          current.right = newNode;
          return this;
        }
        current = current.right;
      }
    }
  }

  // Поиск значения
  search(value) {
    let current = this.root;
    
    while (current) {
      if (value === current.value) return true;
      if (value < current.value) {
        current = current.left;
      } else {
        current = current.right;
      }
    }
    
    return false;
  }

  // Средний обход (Inorder) - рекурсивно
  inorderTraversal(node = this.root, result = []) {
    if (node !== null) {
      this.inorderTraversal(node.left, result);
      result.push(node.value);
      this.inorderTraversal(node.right, result);
    }
    return result;
  }

  // Прямой обход (Preorder)
  preorderTraversal(node = this.root, result = []) {
    if (node !== null) {
      result.push(node.value);
      this.preorderTraversal(node.left, result);
      this.preorderTraversal(node.right, result);
    }
    return result;
  }

  // Обратный обход (Postorder)
  postorderTraversal(node = this.root, result = []) {
    if (node !== null) {
      this.postorderTraversal(node.left, result);
      this.postorderTraversal(node.right, result);
      result.push(node.value);
    }
    return result;
  }

  // Обход в ширину (Level-order)
  levelOrderTraversal() {
    if (!this.root) return [];
    
    const result = [];
    const queue = [this.root];
    
    while (queue.length > 0) {
      const node = queue.shift();
      result.push(node.value);
      
      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }
    
    return result;
  }

  // Найти минимальное значение
  findMin(node = this.root) {
    while (node.left !== null) {
      node = node.left;
    }
    return node.value;
  }

  // Найти максимальное значение
  findMax(node = this.root) {
    while (node.right !== null) {
      node = node.right;
    }
    return node.value;
  }
}

// Пример использования
const bst = new BinarySearchTree();

bst.insert(50);
bst.insert(30);
bst.insert(70);
bst.insert(20);
bst.insert(40);
bst.insert(60);
bst.insert(80);

console.log('Средний обход (Inorder):', bst.inorderTraversal());
console.log('Прямой обход (Preorder):', bst.preorderTraversal());
console.log('Обратный обход (Postorder):', bst.postorderTraversal());
console.log('Обход в ширину (Level-order):', bst.levelOrderTraversal());

console.log('Поиск 40:', bst.search(40)); // true
console.log('Поиск 100:', bst.search(100)); // false

console.log('Минимум:', bst.findMin()); // 20
console.log('Максимум:', bst.findMax()); // 80
