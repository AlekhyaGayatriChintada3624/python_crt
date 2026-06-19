# Calculating area of 3 circles — no functions
r1 = 5
area1 = 3.14159 * r1 * r1
print(area1)
r2 = 7
area2 = 3.14159 * r2 * r2
print(area2)
r3 = 10
area3 = 3.14159 * r3 * r3
print(area3)

print("with functions")
def circle_area(r):
 return 3.14159 * r * r
print(circle_area(5))
print(circle_area(7))
print(circle_area(10))

""" Positional Arguments
Arguments matched by position, left to right."""
def power(base, exponent):
 return base ** exponent

power(2, 10) # base=2, exponent=10
print(power) # 1024