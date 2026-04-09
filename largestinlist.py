arr=list(map(int,input("enter numbers:").split()))
# print(max(arr))
largest=arr[0]
for i in arr:
    if i>largest:
        largest=i
print(largest)
