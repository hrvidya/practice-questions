balance = int(input())

m = int(input())

failed = 0

for i in range(m):

    operation = input().split()

    command = operation[0]
    amount = int(operation[1])

    if command == "DEPOSIT":

        balance += amount

    elif command == "WITHDRAW":

        if balance >= amount:

            balance -= amount

        else:

            failed += 1

print("Final Balance:", balance)
print("Failed Transactions:", failed)
#no variable used