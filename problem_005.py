from functools import reduce
import math

# My first approach - brute force

def smallest_positive_evenly_divisible_by_numbers_from_1_to_20():
	start_number = 1
	n = 20
	divisible = False

	while not divisible:
		divisible = True
		for i in range(1, n+1):
			if start_number % i != 0:
				print(f"start_number: {start_number}")
				start_number += 1
				divisible = False
				break
	return start_number


#print(smallest_positive_evenly_divisible_by_numbers_from_1_to_20())

# prints 232792560 - takes too much time to be a good solution


# My second approach - using the Cake Method (Ladder Method) algorithm
# https://www.calculatorsoup.com/calculators/math/lcm.php

def another_smallest_positive_evenly_divisible_by_numbers_from_1_to_20():
	primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
	lcm_numbers_list = [ i for i in range(1, 21)]

	operations_results = []
	tmp_list = []
	tracker = []

	counter = 0
	prime_index = 0
	continue_loop = True

	while continue_loop:
		prime = primes[prime_index]
		for index, n in enumerate(lcm_numbers_list):
			if n % prime == 0:
				tmp_list.append(n // prime)
				counter += 1
			else:
				tmp_list.append(n)

		print(f"Prime number: {prime}")
		print(f"Occurence counter: {counter}")

		tracker.append((prime, counter))

		if counter >= 2:
			lcm_numbers_list.clear()
			lcm_numbers_list = tmp_list.copy()
			operations_results.append(tmp_list.copy())

		if counter < 2:
			if len(operations_results) > 1:
				lcm_numbers_list = operations_results[-1].copy()
			prime_index += 1

		if counter < 2 and len(tracker) > 1 and tracker[-1][1] < 2 and tracker[-2][1] < 2:
			continue_loop = False

		tmp_list.clear()
		counter = 0

	column = [e[0] for e in tracker[:-2].copy() if e[1] > 1] # tracker[:-2] - remove last 2 elements which are < 2
	if len(operations_results) > 1:
		row = operations_results[-1].copy()
	else: row = operations_results.copy()

	column_vals_multiplied = reduce((lambda x, y: x * y), column)
	row_vals_multiplied = reduce((lambda x, y: x * y), row)
	return column_vals_multiplied * row_vals_multiplied


print(another_smallest_positive_evenly_divisible_by_numbers_from_1_to_20())


#Prime: 2
#Counter: 10
#[1, 1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10]
#
#Prime: 2
#Counter: 5
#[1, 1, 3, 1, 5, 3, 7, 2, 9, 5, 11, 3, 13, 7, 15, 4, 17, 9, 19, 5]
#
#Prime: 2
#Counter: 2
#[1, 1, 3, 1, 5, 3, 7, 1, 9, 5, 11, 3, 13, 7, 15, 2, 17, 9, 19, 5]
#Prime: 3
#Counter: 6
#[1, 1, 1, 1, 5, 1, 7, 1, 3, 5, 11, 1, 13, 7, 5, 2, 17, 3, 19, 5]
#
#Prime: 3
#Counter: 2
#[1, 1, 1, 1, 5, 1, 7, 1, 1, 5, 11, 1, 13, 7, 5, 2, 17, 1, 19, 5]
#
#Prime: 5
#Counter: 4
#[1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 11, 1, 13, 7, 1, 2, 17, 1, 19, 1]
#
#
#Prime: 7
#Counter: 2
#[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 1, 13, 1, 1, 2, 17, 1, 19, 1]
#
#
#
#
#
#
#2 [1, 1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10]
#
#2 [1, 1, 3, 1, 5, 3, 7, 2, 9, 5, 11, 3, 13, 7, 15, 4, 17, 9, 19, 5]
#
#2 [1, 1, 3, 1, 5, 3, 7, 1, 9, 5, 11, 3, 13, 7, 15, 2, 17, 9, 19, 5]
#3 [1, 1, 1, 1, 5, 1, 7, 1, 3, 5, 11, 1, 13, 7, 5, 2, 17, 3, 19, 5]
#
#3 [1, 1, 1, 1, 5, 1, 7, 1, 1, 5, 11, 1, 13, 7, 5, 2, 17, 1, 19, 5]
#
#5 [1, 1, 1, 1, 1, 1, 7, 1, 1, 1, 11, 1, 13, 7, 1, 2, 17, 1, 19, 1]
#
#7 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 11, 1, 13, 1, 1, 2, 17, 1, 19, 1]
#
#
# 2*2*2*3*3*5*7*11*13*2*17*19




# My third approach - using the Greatest Common Factor GCF
# https://www.calculatorsoup.com/calculators/math/lcm.php

def yet_another_smallest_positive_evenly_divisible_by_numbers_from_1_to_20():
	result = 1
	for i in range(1, 21):
		result *= i // math.gcd(i, result)
	return result

print(yet_another_smallest_positive_evenly_divisible_by_numbers_from_1_to_20())
