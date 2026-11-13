n=int(input())
registered=set(map(int,input().split()))
m=int(input())
blocked=0
checked=0
active=set()
for i in range(m):
    operation=input().split()
    command=operation[0]
    vendor_id=int(operation[1])

    if command == 'ENTRY':
        if vendor_id in registered:
            active.add(vendor_id)
        else:
            blocked += 1
    elif command == 'CHECK':
        checked += 1
    elif command == 'EXIT':
        if vendor_id in active:
            active.remove(vendor_id)

print("Active Vendors:", len(active))
print("Blocked Attempts:", blocked)
print("Checked Requests:", checked)