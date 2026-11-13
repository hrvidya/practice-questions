m = int(input())

queue = []

treated = 0

for i in range(m):

    operation = input().split()

    command = operation[0]

    if command == "ARRIVE":

        patient = operation[1]

        queue.append(patient)

    elif command == "TREAT":

        if len(queue) > 0:

            queue.pop(0)

            treated += 1

print("Patients Waiting:", len(queue))
print("Patients Treated:", treated)
#here we are using queue =list because fif0