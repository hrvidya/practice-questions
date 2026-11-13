arr = list(map(int, input("Enter numbers: ").split()))
freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)
#nor
from collections import Counter