n = int(input("enter number:"))

if n < 0:
    print("Factorial not defined for negative numbers")
else:
    factorial = 1
    for a in range(1, n+1):
        factorial *= a
    print(factorial)