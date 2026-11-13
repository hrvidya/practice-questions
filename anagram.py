s1=input("enter string:")
s2=input("enter string:")
if len(s1)!=len(s2):
    print(False)
else:
    count={}
    for ch in s1:
        count[ch]=count.get(ch,0)+1
    for ch in s2:
        if ch in count:
            count[ch]-=1
        else:
            print(False)
            break
    else:
        print(all(v==0 for v in count.values()))

    from collections import Counter
    Counter(s1)==Counter(s2)
    #nor
    sorted(s1)==sorted(s2)
    #LISTEN=SILENT