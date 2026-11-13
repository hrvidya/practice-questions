arr = list(map(int, input("Enter stock prices: ").split()))

# Edge Case: Empty array
if len(arr) == 0:
    print("No prices given")
    exit()

# Edge Case: Only one price
if len(arr) == 1:
    print("Not enough data")
    print("Buy:", arr[0])
    print("Sell:", arr[0])
    print("Profit:", 0)
    exit()

min_price = arr[0]

buy = arr[0]
sell = arr[0]

max_profit = 0

for i in range(1, len(arr)):

    profit = arr[i] - min_price

    # Better profit found
    if profit > max_profit:

        max_profit = profit

        buy = min_price
        sell = arr[i]

    # Update minimum price
    if arr[i] < min_price:
        min_price = arr[i]

# No profit possible
if max_profit == 0:
    print("No profitable transaction possible")

print("Buy:", buy)
print("Sell:", sell)
print("Max Profit:", max_profit)