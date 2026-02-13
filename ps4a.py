# Problem Set 4A
# Name: Alex B
# Collaborators: None

from tree import Node  # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, Node(2, Node(1), Node(6)), Node(10))
tree2 = Node(
    7, Node(2, Node(1), Node(5, Node(3), Node(6))), Node(9, Node(8), Node(10))
)
tree3 = Node(
    5,
    Node(3, Node(2), Node(4)),
    Node(14, Node(12), Node(21, Node(20), Node(26))),
)


def find_tree_height(tree):
    """
    Find the height of the given tree
    Input:
        tree: An element of type Node constructing a tree
    Output:
        The integer depth of the tree
    """
    if tree == None:
        return -1
    else:
        left_height = find_tree_height(tree.get_left_child())
        right_height = find_tree_height(tree.get_right_child())
        max_height = 1 + max(left_height, right_height)
        return max_height


def compare_func_max(child_value, parent_value):
    if child_value < parent_value:
        return True
    else:
        return False


def compare_func_min(child_value, parent_value):
    if child_value > parent_value:
        return True
    else:
        return False


def is_heap(tree, compare_func):
    """
    Determines if the tree is a max or min heap depending on compare_func
    Inputs:
        tree: An element of type Node constructing a tree
        compare_func: a function that compares the child node value to the parent node value
            i.e. op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise
                 op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise
    Output:
        True if the entire tree satisfies the compare_func function; False otherwise
    """
    # ## First working version:
    # # The leaf is a heap
    # if find_tree_height(tree) == 0:
    #     return True

    # # Left child exists, right child doesn't
    # elif tree.get_left_child() != None and tree.get_right_child() == None:
    #     left_child = tree.get_left_child()
    #     if compare_func(left_child.get_value(), tree.get_value()):
    #         if is_heap(left_child, compare_func):
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

    # # Right child exists, left child doesn't
    # elif tree.get_left_child() == None and tree.get_right_child() != None:
    #     right_child = tree.get_right_child()
    #     if compare_func(right_child.get_value(), tree.get_value()):
    #         if is_heap(right_child, compare_func):
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

    # # Both children exist
    # else:
    #     left_child = tree.get_left_child()
    #     right_child = tree.get_right_child()
    #     if compare_func(
    #         left_child.get_value(), tree.get_value()
    #     ) and compare_func(right_child.get_value(), tree.get_value()):
    #         if is_heap(left_child, compare_func) and is_heap(
    #             right_child, compare_func
    #         ):
    #             return True
    #         else:
    #             return False
    #     else:
    #         return False

    ## Gemini's improved logic:
    # Base Case: An empty tree is technically a heap
    if tree is None:
        return True

    left = tree.get_left_child()
    right = tree.get_right_child()

    # 1. Check the Left side
    if left is not None:
        # If the comparison fails OR the subtree isn't a heap, it's False
        if not compare_func(left.get_value(), tree.get_value()) or not is_heap(
            left, compare_func
        ):
            return False

    # 2. Check the Right side
    if right is not None:
        # Same logic for the right
        if not compare_func(
            right.get_value(), tree.get_value()
        ) or not is_heap(right, compare_func):
            return False

    # If we made it through both checks, everything is valid!
    return True
    ## Ask it about "short-circuit" with this task tomorrow!


if __name__ == "__main__":
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    print(find_tree_height(tree1))  # should be 2, it is 2
    print(find_tree_height(tree2))  # should be 3, it is 3
    print(find_tree_height(tree3))  # should be 3, it is 3
