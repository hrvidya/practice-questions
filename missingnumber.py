arr=list(map(int,input("enter numbers:").split()))
n=len(arr)
total=n*(n+1)//2
sum_arr=sum(arr)
duplicate=sum_arr-sum(set(arr))
missing=total-(sum_arr-duplicate)
print(missing)
print(duplicate)

# or

arr = list(map(int, input("Enter numbers: ").split()))
n = int(input("Enter n: "))

total = n*(n+1)//2
sum_arr = 0

for num in arr:
    sum_arr += num

print(total - sum_arr)