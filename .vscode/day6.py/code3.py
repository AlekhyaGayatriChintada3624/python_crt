# nums=[1,2,3,4,5]
# def partition(nums):
# mid=len(nums)//2
# first_part=nums[:mid]
# second_part=nums[mid:]
# print(first_part)
# for i in first_part:
#     print(i)

#print(second_part)
# for i in second_part:
#     print(i)

# def split_list(nums):
#     if len(nums) == 1:
#         print(nums)
#         return

#     mid = len(nums) // 2

#     left = nums[:mid]
#     right = nums[mid:]

#     split_list(left)
#     split_list(right)

# nums= [1, 2, 3, 4, 5, 6]
# print(split_list(nums))

nums=[1,2,3,6,4]
def s(nums):
    if len(nums)==1:
        return nums
    L=len(nums)
    left=nums[:L//2]
    right=nums[L//2:]
    print(s(left),s(right))
    return nums
s(nums)