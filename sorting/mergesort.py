def merge(l1, l2):
	l3 = []
	c1, c2 = 0, 0
	while c1 < len(l1) and c2 < len(l2):
		if l1[c1] < l2[c2]:
			l3.append(l1[c1])
			c1 += 1
		else:
			l3.append(l2[c2])
			c2 += 1


	# merge the remaining of l1 or c2
	if c1 < len(l1):
		l3 = l3 + l1[c1:]

	if c2 < len(l2):
		l3 = l3 + l2[c2:]
	return l3

def mergesort(lst, start, end):
	if end == start:
		return [lst[start]]

	if end < start:
		return []

	split_point = (start + end) // 2
	l1 = mergesort(lst, start, split_point) 
	l2 = mergesort(lst, split_point+1, end)
	l3 = merge(l1, l2) 
	return l3

def mergesort_wrapper(lst):
	return mergesort(lst, 0, len(lst) -1)


l = [1,23,4,5,11, 6,2 ,2,4,4]
l = mergesort_wrapper(l)
print(l)