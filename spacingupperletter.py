s = input()

result = ""

for c in s:

    if c.isupper():
        result += " " + c.lower()

    else:
        result += c

print(result.strip())