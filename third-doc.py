class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1  # Высота

class AVLTree:
    def insert(self, root, key):
        # обычная вставка
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        #  баланс узла
        balance = self.get_balance(root)

        # Левый\левый случай
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Правый\правый случай
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Левый/правый случай
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Правый/левый случай
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        #  вращение
        y.left = z
        z.right = T2

        # обновление высот
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Вернуть новый корень
        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        #  вращение
        y.right = z
        z.left = T3

        # обновление высот
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # Вернуть новый корень
        return y

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def pre_order(self, node):
        if not node:
            return
        print("{0} ".format(node.key), end="")
        self.pre_order(node.left)
        self.pre_order(node.right)

# Пример использования
if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]

    for key in keys:
        root = avl_tree.insert(root, key)

    print("Обход построенного дерева  выполняется так: ")
    avl_tree.pre_order(root)
