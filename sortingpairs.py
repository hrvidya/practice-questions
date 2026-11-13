n = int(input("Enter number of pairs: "))

# Edge Case: Negative number of pairs
if n < 0:
    print("Invalid Input")
    exit()

pairs = []

for i in range(n):

    try:

        a, b = map(int, input(f"Enter pair {i+1}: ").split())

        pairs.append((a, b))

    except:
        print("Invalid pair input")
        exit()

# Edge Case: Empty list
if len(pairs) == 0:
    print("No pairs to sort")
    exit()

# Sort by first element,
# if same then by second element
pairs.sort()

print("Sorted Pairs:")

for pair in pairs:
    print(pair)