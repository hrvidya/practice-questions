s=input("enter a string:")
#if s==s[::-1]:
#   print("palindrome")
#else:
#    print("not palindrome")
rev=""
for ch in s:
    rev=ch+rev
if s==rev:
    print("it is palindrome")
else:
    print("not palindrome")



