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
