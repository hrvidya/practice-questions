def sumdigits(n):

    if n == 0:
        return 0

    return n % 10 + sumdigits(n // 10)

n = int(input())

print(sumdigits(n))
#its a recursive function
#%gives remainder
#//removes last digit
#conntinues and then adds all remainder