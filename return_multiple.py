def infinite_arguments(*args):
	sum = 0
	for arg in args:
		sum += arg
	return sum
sum1 = infinite_arguments(2,3,4,787,9)
print(sum1)
