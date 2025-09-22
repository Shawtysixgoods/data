class TreeNode {
  constructor(value) {
    // Значение узла
    this.value = value;
    // Список дочерних узлов
    this.children = [];
  }

  // Добавление дочернего узла
  addChild(node) {
    this.children.push(node);
  }
}

// Пример использования
const root = new TreeNode("root");
const child1 = new TreeNode("child1");
const child2 = new TreeNode("child2");
root.addChild(child1);
root.addChild(child2);
console.log(root.children.map(c => c.value)); // ["child1", "child2"]