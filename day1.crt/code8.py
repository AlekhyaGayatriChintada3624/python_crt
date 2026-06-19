#Higher Order Functions
#Functions that take other functions as arguments or return functions.

#Python provides three built-in higher order functions:
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# map(func, iterable) — apply func to every element

squares = list(map(lambda x: x**2, numbers))
print(squares) # [1, 4, 9, 16, 25, 36, 49, 64]

# filter(func, iterable) — keep elements where func returns True

evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # [2, 4, 6, 8]

# reduce(func, iterable) — accumulate to single value
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product) # 40320 (8 factorial)