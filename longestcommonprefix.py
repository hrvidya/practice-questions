arr=input().split()
prefix=arr[0]
for word in arr[1:]:
    while not  word.startswith(prefix):
        prefix=prefix[:-1] #remove last character
print(prefix)
        
#flower,flow