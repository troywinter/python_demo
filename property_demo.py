class Demo:
    def __init__(self):
        self._x = None

    @property
    def voltage(self):
        return self._x

    @voltage.setter
    def voltage(self, value):
        self._x = value


class Solution(object):
    @staticmethod
    def license_key_formating(s, k):
        S = s.upper().replace('-', '')
        harry = k if len(S) % k == 0 else len(S) % k
        res = S[:harry]
        while harry < len(S):
            res += '-' + S[harry:harry + k]
            harry += k
        return res


class Node(object):
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class Tree(object):
    def __init__(self):
        self.root = None
        self.dup = list()

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        elif val > node.val:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = Node(val)
        else:
            self.dup.append(val)


def add_to_tree(l: list):
    tree = Tree()
    for i in l:
        tree.add(i)
    print(tree.dup)


if __name__ == '__main__':
    res = Solution.license_key_formating('2-4A0r7-4k', 3)
    print(res)
    add_to_tree([1, 2, 1, 3, 3, 2, 2, 1, 4, 5, 4, 3, 2])
