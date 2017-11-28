# given a tree, write a function to validate if a given tree is a binary search tree



class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def validate_tree(tree):
	if tree is None:
		return True

	if tree.left is not None and tree.left.value > tree.value:
		return False

	if tree.right is not None and tree.right.value < tree.value:
		return False


	return validate_tree(tree.left) and validate_tree(tree.right)



# test code
head = Node(3, Node(1,None), Node(4,None))
head1 = Node(3, Node(4,None), Node(4,None))
head2 = Node(1)
head3 = Node(1,right=Node(2, Node(3), Node(4)))
print(validate_tree(head)) # true
print(validate_tree(head1)) # false
print(validate_tree(head2)) # true
print(validate_tree(head3)) # false
