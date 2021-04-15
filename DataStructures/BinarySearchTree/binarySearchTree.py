# Binary tree is a tree data structure where all its subtrees have only two child nodes
# BST or Binary search tree is a binary tree with some constraints:
#       -> All nodes in the left subtree < root
#       -> All nodes in the right subtree > root
# Traversal : O(log n) Insert : O(log n) , Because each time we half  the number of nodes

# Code snippet below is a python implementation of a BST with insertion & traversal

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
    print("search Result: ", number_tree.search(63))
