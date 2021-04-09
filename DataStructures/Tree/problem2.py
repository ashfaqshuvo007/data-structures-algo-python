# ########### #
# Problem Two #
# ########### #
# Now modify print_tree method to take tree level as input.
# And that should print tree only up to that level as shown below,
# if __name == "__main__":
#    root_node = build_location_tree()
#   root_node.print_tree(1) --> return tree up to level  0
#   root_node.print_tree(2) --> return tree up to level 1
#   root_node.print_tree(3) --> return tree up to level  2

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

    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)


def build_location_tree():
    root = Tree("Global")

    # india
    india = Tree("India")

    gujarat = Tree("Gujarat")
    gujarat.add_child(Tree("Ahmedabad"))
    gujarat.add_child(Tree("Baroda"))

    Karnataka = Tree("Karnataka")
    Karnataka.add_child(Tree("Bengaluru"))
    Karnataka.add_child(Tree("Mysore"))
    india.add_child(gujarat)
    india.add_child(Karnataka)

    # Usa
    usa = Tree("Usa")

    new_jersey = Tree('New jersey')
    new_jersey.add_child(Tree("Princeton"))
    new_jersey.add_child(Tree("Trenton"))
    california = Tree('California')
    california.add_child(Tree("San Francisco"))
    california.add_child(Tree("Mountain view"))
    california.add_child(Tree("Palo Alto"))
    usa.add_child(new_jersey)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root


if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree(3)
