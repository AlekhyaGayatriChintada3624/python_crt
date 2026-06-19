#Without functions:
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

#Problems: code is duplicated, error-prone, not maintainable. If pi's precision changes, you
#update 3 places.
#With functions:

def circle_area(r):
 return 3.14159 * r * r
print(circle_area(5))
print(circle_area(7))
print(circle_area(10))

#One change, everywhere fixed. This is the power of functions.