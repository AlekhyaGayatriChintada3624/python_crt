def merge_lists(L1,L2):
    i,j=0,0
    res=[]
    while i<len(L1) and j<len(L2):
        if L1[i]<L2[j]:
            res.append(L1[i])
            i+=1
        else:
            res.append(L2[j])
            j+=1
    res.extend(L1[i:])
    res.extend(L2[:j])
    return res
ans=merge_lists([1,5,6],[2,4,3,7,9])
print(ans)