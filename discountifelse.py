amount = int(input())

if amount < 1000:

    final = amount - (amount * 0.05)

elif amount < 5000:

    final = amount - (amount * 0.10)

else:

    final = amount - (amount * 0.15)

print(f"{final:.2f}")