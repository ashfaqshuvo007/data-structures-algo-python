# ########### #
# Problem One #
# ########### #
# Extent tree class built in our main tutorial so that it takes name and designation in data part of TreeNode class.
# Now extend print_tree function such that it can print either name tree, designation tree or name and designation tree.
# As shown below,
# Here is how your main function should will look like,
#
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name") # prints only name hierarchy
#     root_node.print_tree("designation") # prints only designation hierarchy
#     root_node.print_tree("both") # prints both (name and designation) hierarchy

class Tree:
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

    def print_tree(self, option):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        if option == 'name':
            print(prefix + self.data.get('name'))
            if self.children:
                for child in self.children:
                    child.print_tree('name')
        elif option == 'designation':
            print(prefix + self.data.get('designation'))
            if self.children:
                for child in self.children:
                    child.print_tree('designation')
        else:
            print(prefix + self.data.get('name') + " (" + self.data.get('designation') + ")")
            if self.children:
                for child in self.children:
                    child.print_tree('both')


def build_management_tree():
    root = Tree({
        'name': 'Nilupul',
        'designation': 'CEO',
    })

    # CTO
    cto = Tree({
        'name': 'Chinmay',
        'designation': 'CTO'
    })

    infra_head = Tree({
        'name': 'Vishwa',
        'designation': 'Infrastructure Head'
    })

    infra_head.add_child(Tree({
        'name': 'Dhaval',
        'designation': 'Cloud Manager'
    }))

    infra_head.add_child(Tree({
        'name': 'Abhijit',
        'designation': 'App Manager'
    }))

    app_head = Tree({
        'name': 'Aamir',
        'designation': 'Application Head'
    })

    cto.add_child(infra_head)
    cto.add_child(app_head)

    # HR  Head
    hr_head = Tree({
        'name': 'Gels',
        'designation': 'HR Head'
    })

    hr_head.add_child(Tree({
        'name': 'Peter',
        'designation': 'Recruitment Manager'
    }))

    hr_head.add_child(Tree({
        'name': 'Waqas',
        'designation': 'Policy Manager'
    }))

    root.add_child(cto)
    root.add_child(hr_head)

    return root


if __name__ == "__main__":
    root_node = build_management_tree()
    # root_node.print_tree("name")  # prints only name hierarchy
    root_node.print_tree("name")
