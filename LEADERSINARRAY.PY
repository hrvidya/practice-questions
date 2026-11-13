arr = list(map(int,input().split()))

if len(arr) == 0:
    print([])
    exit()

leaders = []

max_right = arr[-1]

leaders.append(max_right)

for i in range(len(arr)-2, -1, -1): #-2 because last element already taken,-1 coz  next 0,-1 coz to move backwards

    if arr[i] > max_right:

        max_right = arr[i]

        leaders.append(max_right)

leaders.reverse()

print(leaders)