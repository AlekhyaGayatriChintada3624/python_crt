'''def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

print(bubble_sort(arr))'''
def bubble_sort(nums):
    c=0
    L=len(nums)
    for j in range(L):
        swapped=False
        for i in range(L-1-j):
            c+=1
            
            if nums[i]<nums[i+1]:
                nums[i],nums[i+1]=nums[i+1],nums[i]
                swapped=True
            print(j,i,nums,c)
        if not swapped:
            break
    return nums
nums=[5,4,3,1,2]
print(bubble_sort(nums))