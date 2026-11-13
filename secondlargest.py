arr = list(map(int,input("Enter numbers: ").split()))

if len(arr) < 2:
    print("Second largest not possible")
    exit()

first = second = float('-inf')

for num in arr:

    if num > first:

        second = first
        first = num

    elif num > second and num != first:

        second = num

if second == float('-inf'):
    print("No second largest element")

else:
    print(second)