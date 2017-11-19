# from a single linked list, find the nth element from the last

class Node:
	def __init__(self, num, next_node=None):
		self.num = num
		self.next = next_node
	def __str__(self):
		return str(self.num)

def last_n_from_single_linked_list(head, n):
	# we use two pointers strategy, as it is the most effcient one which
	# does not require additional memory for it to work
	first, previous = head, head
	for i in range(n):
		first = first.next
		if first == None:
			return None   # list is not long enough, so we return None, or ask him about what happens when the list is not long enough
		
	while(1):
		first = first.next
		if first == None: break
		previous = previous.next
	return previous


# test cases
# l = 1 -> 2 -> 3 -> 4 -> 5
l = Node(1,Node(2, Node(3, Node(4, Node(5)))))

print(last_n_from_single_linked_list(l, 1)) # should return 4
print(last_n_from_single_linked_list(l, 0)) # should return 5		
print(last_n_from_single_linked_list(l, 3)) # should return 2
print(last_n_from_single_linked_list(l, 5)) # shoudl return Non
print(last_n_from_single_linked_list(l, 10)) # shoudl return Non