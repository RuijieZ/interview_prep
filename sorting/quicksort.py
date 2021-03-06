import random
import threading
import time
from random import shuffle
from copy import deepcopy

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


"""implementation 2, using the last element in the array as the pivot
"""
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


"""implementation 3 using a random index as the pivot each time
"""
def partition_3(lst, start, end):
	pivot, wall = random.sample(range(start, end+1), 1)[0], start-1
	lst[end], lst[pivot] = lst[pivot], lst[end]
	pivot_value = lst[end]
	for i in range(start, end):
		if lst[i] < pivot_value:
			wall += 1
			lst[wall], lst[i] = lst[i], lst[wall]

	if lst[wall + 1] >= lst[end]:
		lst[wall+1], lst[end] = lst[end], lst[wall+1]

	return wall + 1

def quick_sort_3(lst, start, end):
	if start >= end:
		return
	pivot = partition_3(lst, start, end)
	quick_sort_3(lst, start, pivot-1)
	quick_sort_3(lst, pivot+1, end)



def quick_sort_wrapper_3(lst):
	return quick_sort_3(lst, 0, len(lst)-1)


""" Quick sort implementation 4, using multi-thread to sort the python program
"""
def quick_sort_4(lst, start, end, depth):
	pivot = partition_2(lst, start, end)
	if depth == 3:	# do not create new threads after depth reaches 3
		quick_sort_2(lst, start, pivot-1)
		quick_sort_2(lst, pivot+1, end)
	else:
		t = threading.Thread(target=quick_sort_4, args=(lst,start,pivot-1, depth+1))
		quick_sort_2(lst, pivot+1, end)


def quick_sort_wrapper_4(lst):
	return quick_sort_4(lst, 0, len(lst)-1, 0)



# l= [3,1,2,4,2,2,4]

# test the performance of sequential sorting vs concurrent sorting
l = list(range(1,10000000))
shuffle(l)
l_cp = deepcopy(l)
# quick_sort([1],0,0)
start_time = time.time()
quick_sort_wrapper_4(l)
print("quicksort parellel: --- %s seconds ---" % (time.time() - start_time))
l = deepcopy(l_cp)
start_time = time.time()
quick_sort_wrapper_2(l)
print("quicksort sequential: --- %s seconds ---" % (time.time() - start_time))
from radixsort import radix_sort
l = deepcopy(l_cp)
start_time = time.time()
l=radix_sort(l)
print("Radix sort: --- %s seconds ---" % (time.time() - start_time))
from countingsort import countingsort
l = deepcopy(l_cp)
start_time = time.time()
l=countingsort(l)
print("Counting sort: --- %s seconds ---" % (time.time() - start_time))
from mergesort import mergesort_wrapper_2
l = deepcopy(l_cp)
start_time = time.time()
l=mergesort_wrapper_2(l)
print("mergesort sort parellel: --- %s seconds ---" % (time.time() - start_time))



# print(l)