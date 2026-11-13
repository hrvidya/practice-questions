#maximum sub array
arr=list(map(int,input().split()))
current_sum=arr[0]
max_array=arr[0]
for i in range(len(arr)):
    current_sum=max(arr[i],current_sum+arr[i])
    max_array=max(current_sum,max_array)
print(max_array)
