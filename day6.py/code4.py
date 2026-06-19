'''stack=[5,3,8,2,9]
l=len(stack)
T=8
for i in range(l):
    # print(stack.pop())
    if stack.pop()==T:
        print('found element')
        print(stack)
        break'''

nums=[1,1,1,2,3,4,5]
#sum of all numbers

nums= input()
s=0
for i in nums:
    if i.isdigit():
        s+=int(i)
print(s)