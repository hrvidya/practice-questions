arr=list(map(int,input().split()))
pos=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[pos],arr[i]=arr[i],arr[pos]
        pos+=1#changing position only if it is non zero,so pos is inside if loop
print(pos,i,arr)