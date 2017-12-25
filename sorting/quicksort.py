import random

# implementation 1, using the first element in the array as the pivot
def partition(lst, start, end):
	pivot = start					# select the first one as the pivot
	left, right = start-1, end+1
	while 1:
		left += 1
		while lst[left] < lst[pivot]:
			left += 1

		right -= 1
		while lst[right] > lst[pivot]:
			right -= 1

		if left >= right:
			return right

		lst[left], lst[right] = lst[right], lst[left]

	return pivot


def quick_sort(lst, start, end):
	if start >= end: 
		return
	pivot = partition(lst, start, end)
	quick_sort(lst, start, pivot)
	quick_sort(lst, pivot+1, end)


def quick_sort_wrapper(lst):
	return quick_sort(lst, 0, len(lst)-1)


# implementation 2, using the last element in the array as the pivot
def partition_2(lst, start, end):
	wall, pivot = start-1, end
	for i in range(start, pivot):
		if lst[i] < lst[pivot]:
			wall += 1
			lst[i], lst[wall] = lst[wall], lst[i] 	# put new element inside the "wall" 


	# check if we should put pivot inside the wa
	if lst[wall+1] >= lst[pivot]:
		lst[wall+1], lst[pivot] = lst[pivot], lst[wall+1]

	return wall + 1

def quick_sort_2(lst, start, end):
	if start >= end:
		return

	pivot = partition_2(lst, start, end)
	quick_sort_2(lst, start, pivot-1)
	quick_sort_2(lst, pivot+1, end)

def quick_sort_wrapper_2(lst):
	return quick_sort_2(lst, 0, len(lst)-1)

l= [3,1,2,4,2,2,4]
# quick_sort([1],0,0)
quick_sort_wrapper_2(l)
print(l)