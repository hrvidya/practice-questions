# ==========================================
# PRIME NUMBER
# ==========================================

n = int(input())

if n < 2:
    print("Not Prime")
else:
    flag = True

    for i in range(2, int(n**0.5) + 1):# to check tillroot and ending so add 1

        if n % i == 0:
            flag = False
            break

    print("Prime" if flag else "Not Prime")


# ==========================================
# ARMSTRONG NUMBER
# ==========================================

n = int(input())

temp = n
digits = len(str(n))  #sum of digits whose power raised to len of digits
total = 0

while temp > 0:

    digit = temp % 10

    total += digit ** digits

    temp //= 10

if total == n:
    print("Armstrong")
else:
    print("Not Armstrong")


# ==========================================
# GCD / HCF
# ==========================================

a, b = map(int, input().split())

while b:

    a, b = b, a % b

print(a)


# ==========================================
# LCM
# ==========================================

a, b = map(int, input().split())

x, y = a, b

while b:

    a, b = b, a % b

gcd = a

lcm = (x * y) // gcd

print(lcm)


# ==========================================
# VALID PARENTHESES
# ==========================================

s = input()

stack = []

valid = True

for ch in s:

    if ch in "({[":
        stack.append(ch)

    else:

        if not stack:
            valid = False
            break

        top = stack.pop()

        if ch == ')' and top != '(':
            valid = False

        elif ch == '}' and top != '{':
            valid = False

        elif ch == ']' and top != '[':
            valid = False

if stack:
    valid = False

print(valid)