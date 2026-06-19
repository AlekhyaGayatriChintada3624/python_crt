stack=[5,3,8,2,9]
l=len(stack)
T=8
for i in range(l):
    # print(stack.pop())
    if stack.pop()==T:
        print('found element')
        print(stack)
        break