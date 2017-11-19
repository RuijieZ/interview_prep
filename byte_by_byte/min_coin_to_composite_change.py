# minimum change problem, given an input x, write a function to determine the minimum amount of the coins needed to make that

# 1,5,10,25

# f(x) ->  1 if x  in [1,5,10,25]
#	   ->  min(f(x-1), f(x-5), f(x-10), f(x-25))


# greedy soln
# works because there is a coin 1 inside
coins = [25, 10, 5, 1]

def min_coins_for_change(x, coin_count):
	for coin in coins:
		if x >= coin:
			if x % coin == 0:
				return int(x / coin) + coin_count
			else:
				return min_coins_for_change(x % coin, int(x / coin) + coin_count)


# test
print(min_coins_for_change(100, 0)) # 4
print(min_coins_for_change(99, 0)) # 75 + 20 + 1 * 4  should be 9
print(min_coins_for_change(85, 0)) # 75 + 10   should be 4


# dynanmic programming soln
coins = [25, 10, 5, 1]

def min_coins_for_change_v2(x):
	table = [-1 for i in range(x+1)]
	table[0] = 0
	def min_coin_rec(x):
		if table[x] != -1:
			return table[x]
		else:
			result_lst = [min_coin_rec(x-coin) + 1 if x >= coin else x+1 for coin in coins]
			table[x] = min(result_lst)
			return table[x]
	return min_coin_rec(x)

print(min_coins_for_change_v2(100)) # 4
print(min_coins_for_change_v2(99)) # 75 + 20 + 1 * 4  should be 9
print(min_coins_for_change_v2(85)) # 75 + 10   should be 4
