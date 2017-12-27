from functools import reduce
def radix_sort(lst, base=10):   #bucket sort
	buckets = [[] for i in range(base)]
	if lst == []:
		return
	m, power = max(lst), 0
	while base ** power <= m:
		for item in lst:
			bucket_num = (item // (base ** power)) % base
			buckets[bucket_num].append(item)

		lst = reduce(lambda x,y: x+y, buckets, [])
		buckets = [[] for i in range(base)]
		power += 1
	return lst

if __name__ == "__main__":
	l = [3,4,7,1,1,2,4,13]
	l= radix_sort(l)
	print(l)