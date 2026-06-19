"""stack=[]
stack.append(5)
stack.append(6)
print(stack)
stack.pop()
print(stack)
stack.append(7)
stack.append(4)
print('stack',stack)
print(stack[-1])
print(len(stack)==0)"""
stack=[5,7,6,4,3]
t=3
for i in stack:
    print(i)
    if stack.pop()==t:
        print("found")
print(stack)

    
