class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.value:  # Если ключ меньше, идем в левое поддерево
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:  # Иначе идем в правое поддерево
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.value == key:  # Если узел пустой или значение найдено
            return node
        if key < node.value:  # Если ключ меньше, ищем в левом поддереве
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)  # Иначе ищем в правом

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        res = []
        if node:
            res = self._inorder_traversal_recursive(node.left)  # Обходим левое поддерево
            res.append(node.value)  # Добавляем значение узла
            res = res + self._inorder_traversal_recursive(node.right)  # Обходим правое поддерево
        return res

#  использование
if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(50)
    bst.insert(30)
    bst.insert(20)
    bst.insert(40)
    bst.insert(70)
    bst.insert(60)
    bst.insert(80)

    print("Inorder Traversal:", bst.inorder_traversal())

    # поиск значений
    print("Searching for 40:", bst.search(40) is not None)
    print("Searching for 100:", bst.search(100) is not None)
