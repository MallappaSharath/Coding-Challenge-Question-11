"""
Coding Challenge Question 11 - To print the first 12 "even" Fibonacci numbers
assumption: Fibonacci numbers start from 1 and 1
"""

def print_even_fib(how_many_times):
	"""
		Prints even fibonacci specified number of times
	"""
	
	count = 0
	
	print("The first {count} even Fibonacci numbers:".format(count=how_many_times))
	
	last = 1
	before_last = 1
	
	while count < how_many_times:
		fib = find_next_fib(last, before_last)
		before_last = last
		last = fib
		if fib %2 == 0:
			print(fib)
			count += 1


def find_next_fib(last, before_last):
	"""
		Returns sum of last last two values - i.e., next fibonacci number
	"""
	return last + before_last

how_many_times = int(input("How many even fibonacci numbers do you want to print?:\n"))
print_even_fib(how_many_times)