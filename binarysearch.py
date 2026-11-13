arr=list(map(int,input().split()))
target=int(input())
low=0
high=len(arr)-1
found=-1
while low<=high:
    mid=(low+high)//2
    if target>arr[mid]:
        low=mid+1
    elif target==arr[mid]:
        found=mid
        break
    else:
        high=mid-1
print(found)
