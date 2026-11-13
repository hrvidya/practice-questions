arr = list(map(int,input().split()))

normal = []
tens = []

for num in arr:

    if num % 10 == 0:
        tens.append(num)

    else:
        normal.append(num)

result = normal + tens

print(result)