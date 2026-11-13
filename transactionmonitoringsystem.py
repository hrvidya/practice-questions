n = int(input("Enter number of transactions: "))

transactions = []
seen = set()

for _ in range(n):

    sender, receiver, timestamp, amount = input().split()

    timestamp = int(timestamp)
    amount = int(amount)

    # Full transaction used for duplicate check
    key = (sender, receiver, timestamp, amount)

    if key in seen:
        print("Error: Duplicate Transaction")
        exit()

    seen.add(key)

    transactions.append((timestamp, sender, receiver, amount))

# Sort transactions based on timestamp
transactions.sort()

prev_time = None

for transaction in transactions:

    timestamp = transaction[0]

    if prev_time is not None:

        if timestamp - prev_time > 60:
            print("Fraud Detected")
            exit()

    prev_time = timestamp

print("All Transactions Valid")