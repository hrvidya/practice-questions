n = int(input())

if n <= 0:
    print("Invalid Input")
    exit()

nums = list(map(int,input().split()))

if len(nums) != n:
    print("Input size mismatch")
    exit()

result = 0

for num in nums:
    result ^= num

print(result)