class Node:
	def __init__(self, value, next_n=None):
		self.value = value
		self.next = next_n

	def print_content(self):
		head = self
		while (head != None):
			print(head.value)
			head = head.next

n1 = Node(1)
n2 = Node(2, n1)
n3 = Node(3, n2)
n4 = Node(4, n3)

n4.print_content()

def reverse(head):
	result = None
	while(head != None):
		temp = head.next
		head.next = result
		result = head
		head = temp
	return result			

n4 = reverse(n4)
if n4 is not None:
	n4.print_content()
