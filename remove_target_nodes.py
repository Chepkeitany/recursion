# pylint: disable=R0903
'''
Remove target nodes from a linked list
Time Complexity: O(n) - where n is the number of nodes in the linked list,
                        we need to visit each node once to determine if we
                        should remove it as it matches the target value or not
Space Complexity: O(n) - n is the number of recursive calls in the stack until
                         we reach the base case. Each recursive call takes up
                         additional space in the call stack.
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


def get_list_values(node):
    """Return a list of the values of the linked list in order"""
    result = []
    current = node
    while current:
        result.append(current.data)
        current = current.next

    return result


# Initiliaze linked list 1
head1 = Node(1)
head1.next = Node(5)
head1.next.next = Node(2)
head1.next.next.next = Node(4)
head1.next.next.next.next = Node(3)

print_list(head1)
new_list_head = remove_target_nodes(head1, 2)
assert get_list_values(new_list_head) == [
    1, 5, 4, 3], "Failed to remove node with value 2"

head2 = Node(5)
head2.next = Node(4)
head2.next.next = Node(2)
head2.next.next.next = Node(3)
head2.next.next.next.next = Node(1)

print_list(head2)
assert get_list_values(remove_target_nodes(head2, 3)) == [
    5, 4, 2, 1], "Failed to remove node with value 3"

print("All tests passed!")
