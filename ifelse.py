months = int(input())

if months <= 0:
    print("Invalid Input")

elif months == 1:
    print("Cost:", 2000)

elif months <= 3:
    print("Cost:", 5000)

elif months <= 6:
    print("Cost:", 9000)

else:
    print("Cost:", 15000)