#print all unique pair in the given input
nums=input().split(",")
nums=[7,6,5,4,3,2,1]
for i in range (len(nums)):
    for j in range(i+1, len(nums)):
        print(nums[i],nums[j])
#nums=list(map(int,input().split()))
#for i in range(len(nums)):
#    for j in range(i+1,len(nums)):
#        print(nums[i],nums[j])