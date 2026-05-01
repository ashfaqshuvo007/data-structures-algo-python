
#* Depth First Search (DFS)

#? Create a tree node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#? Create a Tree class
class Tree:
    def __init__(self):
        self.root = None 

    #? Create the tree.
    def create_tree(self, values):
        self.root = Node(values[0])
        self.root.left = Node(values[1])
        self.root.right = Node(values[2])

        #left subtree
        self.root.left.left = Node(values[3])
        self.root.left.right = Node(values[4])

        #Right subtree
        self.root.right.right = Node(values[5])
    
    #? Implement the three types of DFS: Pre-order, In-order, Post-order
    def preorder_traversal(self, root):
        if not root:
            return None
        
        print(root.data, end=" ")
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)
    
    def inorder_traversal(self, root):
        if not root:
            return None
        
        self.inorder_traversal(root.left)
        print(root.data, end=" ")
        self.inorder_traversal(root.right)

    
    def postorder_traversal(self, root):
        if not root:
            return None

        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.data, end=" ")
        


#? function to demonstrate and print the results of thsese three DFS traversals.
if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6]
    tree = Tree()
    tree.create_tree(input)

    print("=========================")
    print("Pre-Order Traversal:")
    tree.preorder_traversal(tree.root)
    print("\n=========================\n")

    print("In-Order Traversal:")
    tree.inorder_traversal(tree.root)
    print("\n=========================\n")

    print("Post-Order Traversal:")
    tree.postorder_traversal(tree.root)
    print("\n=========================\n")