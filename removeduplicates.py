arr=list(map(int,input("Enter numbers:").split()))
#print(list(set(arr)))
res=[]
for i in arr:
    if i not in res:
        res.append(i)
print(res)