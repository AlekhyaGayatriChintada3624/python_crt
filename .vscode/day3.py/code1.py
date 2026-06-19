# Data structures:
# A data structure is a specialized format for organising data in memory 
# that enables effcient storage ,retrival, processing, and manipulation of information
stack=[]
stack.append(5)
stack.append(6)
print(stack)
stack.pop()
print(stack)
stack.append(7)
stack.append(4)
print('stack',stack)
print(stack[-1])
print(len(stack)==0)