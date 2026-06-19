#Lambda Functions
#Anonymous (nameless) functions defined with lambda.
# Syntax: lambda parameters: expression
square = lambda x: x * x
add = lambda x, y: x + y
greet = lambda name: f"Hello, {name}"
print(square(5)) # 25
print(add(3, 4)) # 7
print(greet("Moin")) # Hello, Moin

#When to use lambda: Short, throwaway functions, typically as arguments to higher-order
#functions.

students = [("Moin", 8.9), ("Bob", 7.5), ("Charlie", 9.2)]
# Sort by GPA
sorted_students = sorted(students, key=lambda s: s[1], reverse=True)
print(sorted_students)
# [('Charlie', 9.2), ('Moin', 8.9), ('Bob', 7.5)]
# Filter students with GPA > 8
toppers = list(filter(lambda s: s[1] > 8, students))
print(toppers)
# [('Moin', 8.9), ('Charlie', 9.2)]