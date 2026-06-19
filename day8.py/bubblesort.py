def Bubble_sort(nums):
    l=len(nums)
    c=0
    for j in range(l):
        swapped=False
        for i in range(l-1-j):
            c+=1
            if nums[i]<nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i] 
                swapped=True 
            print(j,i,nums,c)
        if swapped==False:
            break
        
    return nums
nums=[1,2,3,4,5,6]
print(Bubble_sort(nums))