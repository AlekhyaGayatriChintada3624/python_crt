"""what is space complexity?
just like a time complexity measures how long an algorithum takes based on input size N
space complexity measures how much extra memory an algorithum requires as grows.
nums=list(map(int,input().split()))
curr_min=nums[0]
for i in range(len(nums)):
    if curr_min > nums[i]:
        curr_min == nums[i]
print(curr_min)"""

num=int(input())
if num>1:
    if num%2==0:
        print("even positive")
    else:
        print("odd positive")
else:
    if num%2!=0:
        print("even positive")
    else:
        print("odd positive")       