'''What is permutation?
DIFFERENT ARRANGEMENTS OF ELEMENTS.
EXAMPLE:[1,2,3]
POSSIBLE PERMUTATIONS:
[1,2,3]
[1,3,2]
[2,1,3]
[3,1,2]
[3,2,1]
TOTAL =3!=6
WHY LEARN PERMUTATIONS?
USED IN:
>PASSWORD GENERATION
>CRYPTOGRAPHY
>SCHEDULING
>AI SEARCH PROBLEMS
BUILD BACKTRACKING UNDERSTANDING.
HOW TO GENERATE PERMUTATIONS (BACKTRACKING):'''


##def permute (num, path=[]):
##    if len(path)==len(nums):
##        print(path)
##        return
##    for num in nums:
##        if num not in path:
##            permute(nums, path +[num])
##
##nums=list(map(int, input("enter ur numbers to generate elements in different sequence:").split(",")))
##permute(nums)


'''N-QUEENS ALGORITHUM:
    WHAT IS N-QUEENS?
    PLACE N QUEENS ON NXN CHESSBOARD SUCH THAT
    >NO TWO

'''

##
##def solve_n_queens(n):
##    board=[-1]*n
##    def is_safe(row, col):
##        for i in range(row):
##            if board[i]==col:
##                return False
##        return True
##    def backtrack(row):
##        if row==n:
##            print(board)
##            return
##        for col in range(n):
##            if is_safe(row, col):
##                board[row]=col
##                backtrack(row+1)
##                board[row]-1
##
##    backtrack(0)
##solve_n_queens(4)


'''TWO POINTER & SLIDING WINDOW SUBARRAY PROBLEMS:
WHAT IS TWO POINTER>
INSTEAD OF USING TWO NESTED LOOPS (0(N^)) , FOR TWO INDICES TO REDUCE TIME COMPLEXITY TO 0(N).
REAL-LIFE EXAMPLE:
IMAGINE YOU AND YOUR FRIEND ARE SEARCHING FORTWO STUDENTS WHOSE TOTAL HEIGHT=170CM
>YOU STAND AT THE SHORTEST STUDENT.
>YOUR FRIEND STANDS AT THE TALLEST STUDENT.
>IF SUM IS SMALL-> MOVE FORWARD.
>IF SUM IS LARGER -> MOVE BACKWARD.
PAIR SUM(SORTED ARRAY):
FIND TWO NUMBERS WHOSE SUM= TARGET.'''
##
##def pair_sum(arr, target):
##    left=0
##    right=len(arr)-1
##    while left<right:
##        current_sum=arr[left]+arr[right]
##        if current_sum==target:
##            return arr[left],arr[right]
##        elif current_sum<target:
##            left+=1
##        else:
##            right+=1
##    return None
##arr=list(map(int, input("enter ur list:").split(",")))
##print(pair_sum(arr, 30))

##time complexity=o(n)



'''SLIDING WINDOW TECHNIQUE:
WHAT IS SLIDING WINDOW?
USED WHEN:
>SUBARRAY
>SUBSTRING
>CONTINUOUS ELEMENT
>longest/smallest/maximum window

maximum sum sub array of size k:
problem:
find maximum sum of k consecutive element:


arr=[2,1,4,5,6,7,9]
k=3
find the maximum sum of 3 consequtive elemnts.
what we need: we need sum of every subarray of size
[2,1,4]
[1,4,5]
[4,5,6]
[5,6,7]
[6,7,9]

'''
##def max_subarray_sum(arr, k):
##    window_sum=sum(arr[:k])
##    max_sum=window_sum
##    for i in range(k,len(arr)):
##        window_sum+=arr[i]-arr[i-k]
##        max_sum=max(max_sum, window_sum)
####    return max_sum
##    return arr[k:i+1]
##arr=list(map(int, input("enter ur list:").split(",")))
##print(max_subarray_sum(arr, 3))


'''longest substring without repeating characters:'''

##def longest_substring(s):
##    char_set=set()
##    left=0
##    max_lenghth=0
##    for right in range(len(s)):
##        while s[right] in char_set:
##            char_set.remove(s[left])
##            left+=1
##        char_set.add(s[right])
##        max_length=max(max_length,right-left+1)
##    return max_length
##s=input("enter ur substring:")
##print(longest_substring(s))




#
#HASHING AND PREFIX SUM:
##What is hashing?
##hashing means:
##Sorting data in key--> value format for fast lookup (0(1)) time.
##in python:
##>dict
##>collection .Counter
##>set
##Why Hashing is important in interviews?
##Because hashing helps to:
##    >count frequencies.
##    > Detect duplicates
##    >solve anagrams
##    >solve subarray problems
##    >optimize brute -force solutions(0(n^2))-->0((n))
##What is Frequency Map?
##It store: element --> number of times it appears.
##
##Example1:  Count character frequency.

##s=input("enter ur string to cal frequency:")
##def char_frequency(s):
##    freq={}
##    for ch in s:
##        freq[ch]=freq.get(ch,0)+1
##    return freq
##print(char_frequency(s))


####what does freq.get(key, default):
##give me the valueof key if it exists, otherwise return default value.
##freq.get(ch,0):
##    if ch is already exist:-. return its count.
##    if ch does not exists:->return 0
##    why +1:
##        because we are counting frequency.
##        every time we see a character.
##        if it's new-> count should starts from 1
##        if it's already there -> increases count by 1.



##PREFIX SUM:
##what is Prefix Sum?
##Prefix sum Means:->  Running cummulative sum of array elements
##arr=[11,2,3,4]
##Prefix Sum:
##    [1,3,6,10]
##    why prefix sum is important?
##    use for:->
##    >subarray sum problems
##    >range sum queries
##    >optimization problem


def subarray_sum(arr, target):
    prefix_sun=0
    seen=set()
    for num in arr:
        prefix_sum+=num
        if prefix_sum==target:
            return True
        if(Prefix_sum_target) in seen:
            return True
        seen.add(prefix_sum)
        return False
arr=list(map(int, input("enter ur list:").split(",")))
target=int(input("enter ur target value:"))
print(subarray_sum(arr, target))

