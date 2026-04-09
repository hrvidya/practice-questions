s=input("enter string:")
#print(sum(1 for ch in s if ch in "aeiouAEIOU"))
count=0
for ch in s:
    if ch in "aeiouAEIOU":
        count+=1
print(count)