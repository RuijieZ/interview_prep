def selection_sort(lst):
	if lst == []:
		return
	end = len(lst)
	for i in range(end):
		cur_min, min_pos = lst[i],i
		for j in range(i,end):
			if lst[j] < cur_min:
				cur_min, min_pos = lst[j], j

		if min_pos != i:
			lst[i], lst[min_pos] = lst[min_pos], lst[i]

l= [3,1,2,4,2,2,4]
# quick_sort([1],0,0)
selection_sort(l)
print(l)