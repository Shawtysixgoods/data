class _Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        # Высота узла — это количество шагов вниз до самого дальнего листа.
        # У нового узла без детей высота всегда равна 1.
        self.height = 1

class AVLTree:
    def __init__(self):
        self._root = None

    def insert(self, key):
        # Вставляем элемент и при необходимости обновляем корень всего дерева,
        # так как после балансировки на самый верх может подняться другой узел.
        self._root = self._insert(self._root, key)

    # --- Вспомогательные расчёты ---

    def _height(self, node):
        # Если узла нет (пустота), его высота равна 0.
        return node.height if node else 0

    def _update_height(self, node):
        # Высота любого узла — это высота самого длинного его поддерева + 1 шаг до него самого.
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        # Считаем разницу высот между левой и правой стороной.
        # Идеальный баланс = 0. Допустимый перекос = -1 или 1.
        # Если получилось 2 или -2 — одна ветка вытянулась слишком сильно, пора балансировать.
        return self._height(node.left) - self._height(node.right) if node else 0

    # --- Повороты: перевешиваем ветки, не нарушая порядок чисел ---

    def _rotate_right(self, node):
        # Левая сторона перевесила. Поднимаем левого ребёнка на место текущего узла,
        # а сам текущий узел опускаем вправо (ведь его число больше).
        new_root = node.left
        moved_subtree = new_root.right  # Это поддерево зажато по значению между ними

        new_root.right = node
        node.left = moved_subtree  # Перевешиваем зажатое поддерево на освободившееся место

        # Пересчитываем высоты: сначала у того, кто опустился вниз, потом у нового лидера.
        self._update_height(node)
        self._update_height(new_root)
        return new_root

    def _rotate_left(self, node):
        # Правая сторона перевесила. Поднимаем правого ребёнка на место текущего узла,
        # а сам текущий узел опускаем влево (ведь его число меньше).
        new_root = node.right
        moved_subtree = new_root.left  # Поддерево, зажатое по значению между ними

        new_root.left = node
        node.right = moved_subtree

        self._update_height(node)
        self._update_height(new_root)
        return new_root

    # --- Главная логика балансировки ---

    def _rebalance(self, node):
        # Смысл балансировки: не дать дереву вытянуться в длинную «палку»,
        # из-за которой поиск стал бы медленным. Мы выравниваем высоты веток.
        self._update_height(node)
        balance = self._balance_factor(node)

        # 1. Левая ветка длиннее правой на 2 уровня
        if balance > 1:
            # Если ветка изогнута зигзагом (сначала влево, потом вправо),
            # одним поворотом её не выпрямить — сначала выравниваем левую часть.
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            # Теперь ветка прямая, поворачиваем весь узел вправо и выравниваем высоты.
            return self._rotate_right(node)

        # 2. Правая ветка длиннее левой на 2 уровня
        if balance < -1:
            # Если ветка изогнута зигзагом (сначала вправо, потом влево),
            # сначала выпрямляем правую часть.
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            # Поворачиваем узел влево, чтобы распределить высоту равномерно.
            return self._rotate_left(node)

        # Перекоса нет — оставляем узел как есть.
        return node

    def _insert(self, node, key):
        # Ищем свободное место внизу дерева, как в обычном бинарном дереве поиска
        if not node:
            return _Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        # Возвращаясь после вставки снизу вверх к корню, проверяем каждый узел
        # и сразу чиним баланс там, где он нарушился.
        return self._rebalance(node)


if __name__ == "__main__":
    tree = AVLTree()
    # Вставляем числа строго по возрастанию.
    # Обычное дерево превратилось бы в линию 10 -> 20 -> 30,
    # но AVL-дерево сделает левый поворот и поставит 20 в корень.
    for number in [10, 20, 30]:
        tree.insert(number)

    print("Корень дерева:", tree._root.key)         # 20
    print("Левый ребёнок:", tree._root.left.key)    # 10
    print("Правый ребёнок:", tree._root.right.key)  # 30

