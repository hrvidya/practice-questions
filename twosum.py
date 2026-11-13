#edge cases
arr = list(map(int,input().split()))

if len(arr) < 2:#len of array
    print(-1)
    exit()

arr.sort()

target = int(input())

left = 0
right = len(arr)-1

found = False

while left < right:

    current_sum = arr[left] + arr[right]

    if current_sum == target:
        print(arr[left], arr[right])
        found = True
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1

if not found:
    print(-1)
#or
arr = list(map(int,input().split()))
target = int(input())

seen = set()

for num in arr:

    complement = target - num

    if complement in seen:
        print(complement, num)
        break

    seen.add(num)

else:
    print(-1)