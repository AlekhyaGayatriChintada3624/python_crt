
nums=input().split(",")
print(nums)
for i in range(len(nums)):
    if i%2==0:
        nums[i]=int(nums[i])*2
    else:
        nums[i]=int(nums[i])*3

print(nums)
        


