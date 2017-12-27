def countingsort(lst):
	m = max(lst)
	count = [0 for i in range(m+1)]
	for i in lst:
		count[i] += 1

	result = []
	for index, item in enumerate(count):
		if item != 0:
			for i in range(item):
				result.append(index)

	return result


l = [0, 19, 7, 3, 2, 1, 3, 4, 7, 6]
l = countingsort(l)
print(l)



