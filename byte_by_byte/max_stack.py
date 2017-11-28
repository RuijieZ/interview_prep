# design a stack with pop push and max function with all the above 3 operations have the same run time to be O(1)

# we are gonna implement this as a linked list, with each node store three informations
# 1. next node
# 2. value of this node
# 3. value of the max so far

class Node:
	def __init__(self, element, next_node=None, max_so_far=None):
		self.element = element
		self.next_node = next_node
		self.max_so_far = max_so_far


class MaxStack(object):
	"""docstring for MaxStack"""
	def __init__(self):
		self.head = None

	def push(self, element):
		if self.head is None:
			self.head = Node(element, max_so_far=element)
		else:
			if element > self.head.max_so_far:
				self.head = Node(element, self.head, max_so_far= element)
			else:
				self.head = Node(element, self.head, max_so_far=self.head.max_so_far)



	def pop(self):
		if self.head is None:
			return None

		value = self.head.element
		self.head = self.head.next_node
		return value

	def max(self):
		return self.head.max_so_far


# test
ms = MaxStack()
ms.push(1)
ms.push(2)
ms.push(3)
print(ms.max()) # 3
print(ms.pop()) # 3
print(ms.max()) # 2
print(ms.pop()) # 2
print(ms.max()) # 1
ms.push(4)
print(ms.max()) # 4
