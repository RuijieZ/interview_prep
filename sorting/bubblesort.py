def bubble_sort(lst):
	while 1:
		swapped = False
		for i in range(len(lst) -1):
			if lst[i] > lst[i+1]:
				lst[i], lst[i+1] = lst[i+1], lst[i]
				swapped = True

		if not swapped:
			return


# test
l = [2,3,1,1,3,2,4,4,5]
bubble_sort(l)
print(l)