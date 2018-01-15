class Node:
	def __init__(self, value, next_n=None):
		self.value = value
		self.next = next_n





n1 = Node(1)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)
n1.next = n4    # create a cycle

def find_cycle(head):
	if head is None:
		return False

	cpy = head
	while(1):
		head = head.next
		cpy = cpy.next
		if cpy is None:
			return False
		else:
			cpy = cpy.next

		if cpy is None:
			return False

		if cpy == head:
			return True

print(find_cycle(n4))   # expect true
print(find_cycle(n3))   # expect true
n1.next = None
print(find_cycle(n4))   # expect false
