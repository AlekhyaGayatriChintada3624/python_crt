#sum of square of the numbers
#square of all numbers
nums=input().split()
s=0
for i in nums:
    x=(int(i)*int(i))
    s+=x
    print(x)
print(s)