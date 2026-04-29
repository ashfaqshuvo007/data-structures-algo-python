
# Code snippet for implementation of tree. taking the scenario of a electronics shop hierarchy as an example
from collections import deque
class Tree:
    # initialize a node with data,parent and child
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = Tree("Electronics")

    laptop = Tree("Laptop")
    laptop.add_child(Tree("Macbook"))
    laptop.add_child(Tree("Surface"))
    laptop.add_child(Tree("Dell"))
    laptop.add_child(Tree("Thinkpad"))

    cellphone = Tree("Cellphone")
    cellphone.add_child(Tree("Iphone"))
    cellphone.add_child(Tree("Vivo"))
    cellphone.add_child(Tree("Samsung"))
    cellphone.add_child(Tree("Xiomi"))

    tv = Tree("TV")
    tv.add_child(Tree("LG"))
    tv.add_child(Tree("Panasonic"))
    tv.add_child(Tree("Hisense"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root

#TODO: Need to implement this.

def breadth_first_search(root, target):
    # First add elements to a queue
    queue = deque()
    graph = {}
    graph[root]
    visited = set() # To keep track of visited nodes

    while queue:
        curr = queue.popleft()
        if curr == target:
            return True
        else:
            if curr not in visited:
                breadth_first_search(curr.children, target)
                visited.add(curr)
    return False


if __name__ == '__main__':
    tree = build_tree()
    breadth_first_search(tree, "Panasonic")
