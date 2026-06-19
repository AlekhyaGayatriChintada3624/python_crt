nums=input().split()
L=len(nums)
#nums.reverse()
#nums=nums[::-1]
L1=[]
for i in range(1,L+1):
    L1.append(nums[L-1])
nums=L1
for i in range(L):
    for j in range(i+1,L):
        print(nums[L-i-1],nums[L-i-j])

#print(L1)