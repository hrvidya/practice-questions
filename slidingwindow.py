arr = list(map(int,input().split()))

if len(arr) == 0:
    print("Empty Array")
    exit()

k = int(input())

if k <= 0 or k > len(arr):
    print("Invalid Window Size")
    exit()

window_sum = sum(arr[:k])

max_sum = window_sum

for i in range(k, len(arr)):

    window_sum = window_sum - arr[i-k] + arr[i]

    if window_sum > max_sum:
        max_sum = window_sum

print(max_sum)