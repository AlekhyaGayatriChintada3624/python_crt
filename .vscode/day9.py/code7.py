numbers = list(map(int, input("Enter the list of numbers: ").split(",")))
def Add(numbers):
    sum=0
    if len(numbers) == 0:
        print("zero numbers are present in list",numbers)
        return 0
    
    for i in numbers:
        sum += i
        return sum
    
print(Add(numbers))

name=str(input("enter ur input:"))
def countchr(name):
    count=0
    if len(name)==0:
        return 0
    else:
        for ch in name:
            if ch==name[ch]:
                count+=1
                print(ch,count)
                countchr(ch-1)
            return count
        
        
countchr(name)
