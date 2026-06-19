'''def sum_list(numbers):
    if len(numbers)==0:
        return 0
    else:
        return numbers[0]+sum_list(numbers[1:])
my_list=[1,2,3,4,5]
print(sum_list(my_list ))'''
'''Recursion:
Recursion is a problem sloving technique where a function sloves a problem 
by calling itself on a smaller version of the same problem 
until a stopping condition (base case) is reached.'''

'''for i in range(10,1,-1):
    print(i)'''

'''i=20
while i>10:
    print(i-10)
    i-=1
    
    print(9)
    print(8)
    print(7)
    print(6)
    print(5)
    print(4)
    print(3)
    print(2)
    print(1)'''

'''def count(n):
    if n==0:
        return
    print(n)
    count(n-1)
count(10)

def Hello():
    for i in range(5):
        print(i)
        if i==2:
            return 
    print('Hello')
Hello()'''

def odd_even(n):
    if (n%2==0):
        return "even"
    return "odd"
print(odd_even(43))