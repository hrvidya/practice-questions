s = input()

count = 0
ans = 0

for ch in s:

    if ch == '1':

        count += 1

    else:

        ans += count * (count + 1) // 2

        count = 0

ans += count * (count + 1) // 2

print(ans)