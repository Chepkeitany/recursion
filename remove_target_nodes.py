# pylint: disable=R0903
'''
Remove target nodes from a linked list
'''

class Node:
    """Class to represent a node in a linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_target_nodes(node, target):
    """Remove target nodes from the linked list"""
    # Base case: If the current node is None, just return None
    if not node:
        return None

    # Recursive case: process the next node
    node.next = remove_target_nodes(node.next, target)

    if node.data == target:
        return node.next
    return node

def print_list(node):
    """Print out the values of the linked list"""
    current = node
    while current:
        print(current.data, end=" ")
        current = current.next
    print()

# Initiliaze linked list 1
head1 = Node(1)
head1.next = Node(5)
head1.next.next = Node(2)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(3)

print_list(head1)
new_list_head = remove_target_nodes(head1, 2)
print_list(new_list_head)
