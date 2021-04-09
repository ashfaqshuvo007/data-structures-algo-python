# Tree is a recursive data structure i.e. all the child nodes are trees as well
# It has many levels and parent/child relation among the levels
# root Node has a level of 0 and it increases as we add children to the tree
# the leaf Nodes have ancestors till we get to root.


# Code snippet for implementation of tree. taking the scenario of a electronics shop hierarchy as an example

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

    root.print_tree()


if __name__ == '__main__':
    build_tree()
