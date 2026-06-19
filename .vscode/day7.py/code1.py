##INSERSTION SORT:
'''Inserstion sort is a simple comparistion-based sorting algorithum.
It works like sorting playing card in your hand.
You pick one card at a time and insert it into its correct position among already sorted cards.
*process:
    Divide the array into:
    sorted part(left)
    Unsorted part (right side)
    Pick one element from unsorted part.
    place it in the correct position in sorted part.
    Repeat until entire array is sorted.'''
#Inserstion sort algorithum implementation with python:
##def insertion_sort(arr):
##    n=len(arr)
##    for i in range(1,n):
##        key=arr[i]
##        j=i-1
##        while j>=0 and arr[j]>key:
##            arr[j+1]=arr[j]
##            j-=1 
##        arr[j+1]=key
##    return(arr)
##print(insertion_sort([5,6,8,9,3,7,2])) 
##


##QUICK SORT:
'''Quick sorr is one of the fastest sorting algorithum in practice.
It follows a powerful technique called:
    >Divide the array.
    >Solves smaller parts
    >Combine results automatically.
    ALGOGITHUM:
        1.Pick one element--> called pivot
        2. put:
            >Smaller element on left
            >larger element on right.
        3.Repeat the same process for left and right parts'''

##PYTHON CODE:
##def quick_sort(arr):
##    if len(arr)<=1:
##        return arr
##    pivort=arr[-1]
##    left=[]
##    right=[]
##    for i in range(len(arr)-1):
##        if arr[i]<pivort:
##            left.append(arr[i])
##        else:
##            right.append(arr[i])
##    return quick_sort(left)+[pivort]+quick_sort(right)
##arr=list(map(int,input("eneter ur list:").split(",")))
##print(quick_sort(arr))

'''programs on subsets:
## GIVEN TWO LISTS,CHECK WHETHER LIST B IS A SUBSET OF LIST A.
## EXAMPLE:'''
##A=list(map(int,input("eneter ur list:").split(",")))
##B=list(map(int,input("eneter ur list:").split(",")))
##def is_subset(A,B):
##    for element in B:
##        if element in A:
##            return True
##    return False
##print(is_subset(A,B))

##'''GENERATE ALL POSIBLE SUBSETS IN A GIVEN LIST:-
##EXAMPLE:-
##INPUT:- [1,2]
##OUTPUT:- [[],[1],[2],[1,2]]
##PROGRAM:-
##'''
##nums=list(map(int,input("enter ur list:").split(",")))
##def generate_subset(nums):
##    subset=[[]]#start with empty subset
##    for num in nums:
##        new_subsets=[]
##        for subset in subsets:
##            new_subsets.append(subset + [num])
##             subset.extend(new_subset)
##        return subset
##print(nums)            
##    
##print(generate_subset(nums))
##           

'''RECURSTION:
    WHAT IS RECURSTION?
    RECURSTION IS WHEN A FUNCTION CALLS ITSELF TO SOLVE A SMALLER VERSTION OF THE SAME PROBLEM
    BIG-PROBLEM --> BREAK INTO SMALLER

EXAMPLE:
    5!=5*4!
    5=5*4*3!
    5=5*4*3*2!
    5=5*4*3*2*1!
    FACTORIAL(n)=n*factorial(n-1)'''
inp=int(input("enter a value:"))
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)
print(factorial(inp))

    


