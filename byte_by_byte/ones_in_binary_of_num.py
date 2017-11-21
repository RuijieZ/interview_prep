# take a number. return how many 1s' in its binary representation

# keep devide by 2, if remediander is 1, then it contains 1

def ones_in_binary_representation(x):
	count = 0
	while x != 0:
		if x & 1 == 1:  # bitwise and, we could use  x % 2 ==1, but bit operation si faster
			count += 1
		x = x >> 1		#  bitshift to the right by 1 place, we could use x = x // 2

	return count


# test
print(ones_in_binary_representation(0)) # 0
print(ones_in_binary_representation(1)) # 1
print(ones_in_binary_representation(2)) # 1
print(ones_in_binary_representation(8)) # 1
print(ones_in_binary_representation(7)) # 3
