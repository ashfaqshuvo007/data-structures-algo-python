# Binary tree is a tree data structure where all its subtrees have only two child nodes

# Problem:
# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calculates sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): performs pre order traversal of a binary tree

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # if root has the data, we skip as bst does not allow  duplicate values
        if data == self.data:
            return
        # if parent is less than incoming data, add it to left subtree
        if data < self.data:
            # if left subtree exists
            if self.left:
                # removes duplicate
                self.left.add_child(data)
            else:
                # add data to left
                self.left = BST(data)
        else:
            # add it to right subtree
            if self.right:
                # removes duplicate
                self.right.add_child(data)
            else:
                # add data to right
                self.right = BST(data)

    def in_order_traversal(self):
        # declare an empty list
        elements = []

        # visit left subtree
        if self.left:
            # goes to the last left leaf node and completes left subtree
            elements += self.left.in_order_traversal()
        # visit root node
        elements.append(self.data)

        if self.right:
            # visit right subtree
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        # check if val is the root
        if self.data == val:
            return True
        # check left subtree
        if val < self.data:
            # check it has left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        # check right subtree
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    # find the max element
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    # find the min element
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        elements = self.in_order_traversal()
        total = 0
        for i in range(0, len(elements)):
            total += elements[i]
        return total

    # Post order Traversal
    def post_order_traversal(self):
        # declare an empty list
        elements = []

        # traverse the left subtree
        if self.left:
            elements += self.left.post_order_traversal()
        # traverse the right subtree
        if self.right:
            elements += self.right.post_order_traversal()

        # visit the root node
        elements.append(self.data)

        return elements

    # Pre order traversal
    def pre_order_traversal(self):
        #  declare an empty list
        elements = [self.data]

        # visit the root node

        # Visit the left tree
        if self.left:
            elements += self.left.pre_order_traversal()

        # Visit the right subtree
        if self.right:
            elements += self.right.pre_order_traversal()
        return elements


def build_tree(element_list):
    # add the first element to root for now
    root = BST(element_list[0])

    # from 1st index to end of list add to the tree
    for i in range(1, len(element_list)):
        root.add_child(element_list[i])

    # return the trees
    return root


if __name__ == "__main__":
    number_list = [18, 15, 12, 13, 25, 21, 24]
    number_tree = build_tree(number_list)
    print(number_tree.in_order_traversal())
    print("=================")
    print("Max value: ", number_tree.find_max())
    print("=================")
    print("Min value: ", number_tree.find_min())
    print("=================")
    print("Sum: ", number_tree.calculate_sum())
    print("=================")
    print("Post Order Traversal: ", number_tree.post_order_traversal())
    print("=================")
    print("PRE Order Traversal: ", number_tree.pre_order_traversal())
