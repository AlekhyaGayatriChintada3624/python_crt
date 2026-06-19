#factorial of a number
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# num=int(input("enter ur number"))
# print(factorial(num))
num=int(input('enter ur number'))
fact = 1
i = 1

while i <= num:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)