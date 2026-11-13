m = int(input())

inventory = {}

failed = 0

for i in range(m):

    operation = input().split()

    command = operation[0]
    item = operation[1]
    quantity = int(operation[2])

    if command == "ADD":

        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity

    elif command == "REMOVE":

        if item in inventory and inventory[item] >= quantity:

            inventory[item] -= quantity

        else:

            failed += 1

total_items = 0

for item in inventory:

    total_items += inventory[item]

print("Total Items:", total_items)
print("Failed Requests:", failed)
#used dictionary