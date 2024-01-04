# TreeNode class
class TreeNode:
    def __init__(self, value):
       self.value = value
       self.left = None
       self.right = None

'''
Insert a node into a BST following the BST properties
For any given node with a key, all keys in the left subtree are less than the node's key,
and all keys in the right subtree are greater than the node's key.
This property must hold true for every node in the tree.

Time Complexity: O(h) where h is the height of bst. In the worst case, 
                      the bst looks like a linked list so h is equal to
                      the number of nodes in the bst. So the time complexity
                      becomes O(n). For a balanced bst, time complexity is
                      O(log n)
Space Complexity: O(h) The function will make h recursive calls until it finds
                       a location to insert the new node.
'''
def insert_bst(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert_bst(root.left, value)
    if value > root.value:
        root.right = insert_bst(root.right, value)

    return root

def print_bst_inorder(node):
    if not node:
        return

    print_bst_inorder(node.left)
    print(node.value, end=" ")
    print_bst_inorder(node.right)

'''
Traverse BST inorder and return the node values in the order they were visited
Time Complexity: O(n)  - where n is the number of nodes that we will visit in the tree
Space Complexity: O(h) - where h is the height of the tree. We will make 
                         h recursive calls as we're traversing the tree in order
                         in a balanced tree, this will be logarithmic but 
                         in a tree that is skewed to one side and looks like a
                         linked list, this will lead to n recursive calls
'''
def inorder_traversal(node, inorder_list):
    if not node:
        return
    inorder_traversal(node.left, inorder_list)
    inorder_list.append(node.value)
    inorder_traversal(node.right, inorder_list)

# Initialize BST
root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
root.left.right = TreeNode(5)
root.right.right = TreeNode(9)

# Insert 4
root = insert_bst(root, 4)
inorder_list = []
inorder_traversal(root, inorder_list)
assert inorder_list == [1, 3, 4, 5, 6, 8, 9], "Failed to correctly insert 4 into the bst"

# Insert 7
root = insert_bst(root, 7)
inorder_list = []
inorder_traversal(root, inorder_list)
assert inorder_list == [1, 3, 4, 5, 6, 7, 8, 9], "Failed to correctly insert 7 into the bst"

print("All tests passed!")
