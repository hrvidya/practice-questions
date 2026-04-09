
s=input("enter a string:")
rev =""
#rev=s[::-1]
#print(rev)
for ch in s:
    rev=ch+rev 
print(rev)
