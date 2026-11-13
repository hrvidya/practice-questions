n = int(input())
#check in case of 0

if n % 2 == 1:

    print(2 ** (n // 2))

else:

    print(3 ** ((n // 2) - 1))