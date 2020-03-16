'''
 시간복잡도 : O(log(n)), worst: O(n) (=> 편향된 트리)
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node

    def find(self, data):
        return self._find_value(self.root, data)

    def _find_value(self, root, data):
        if root is None or root.data == data:
            return data
        elif data < root.data:
            return self._find_value(root.left, data)
        else:
            return self._find_value(root.right, data)

    def get_height(self, root):
        if root is None:
            return -1

        left_height = self.get_height(root.left) + 1
        right_height = self.get_height(root.right) + 1

        return max(left_height, right_height)

    def delete(self, data):
        self.root, deleted = self._delete_value(self.root, data)
        return deleted

    def _delete_value(self, node, data):
        if node is None:
            return node, False

        deleted = False
        if data == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                # 오른쪽 서브트리의 가장 왼쪽 아래에 위치한 자손을 가져옴
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left

                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif data < node.data:
            node.left, deleted = self._delete_value(node.left, data)
        else:
            node.right, deleted = self._delete_value(node.right, data)
        return node, deleted

    # root - left - right
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data)
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

    # left - root- right
    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data)
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)

    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data)
        _post_order_traversal(self.root)

    def level_order_traversal(self):
        def _level_order_traversal(root):
            queue = [root]
            while queue:
                root = queue.pop(0)
                if root is not None:
                    print(root.data)
                    if root.left:
                        queue.append(root.left)
                    elif root.right:
                        queue.append(root.right)
        _level_order_traversal(self.root)

if __name__ == '__main__':
    array = [40, 4, 34, 45, 14, 55, 48, 13, 15, 49, 47]

    bst = BinarySearchTree()

    root = None
    for x in array:
        root = bst.insert(x)

    height = bst.get_height(root)
    print(height)

    value = bst.find(15)
    print(value)

    bst.pre_order_traversal()
    print('-'*30)
    bst.in_order_traversal()
    print('-' * 30)
    bst.post_order_traversal()
    print('-', 30)
    bst.level_order_traversal()
    # ind_value = bst.find(4)
    # print(find_value)