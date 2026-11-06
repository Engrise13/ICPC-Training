import sys

case_num = int(sys.stdin.readline())
lengths = []
elems = []

for i in range(case_num):
    lengths.append(int(sys.stdin.readline()))
    elems.append(sys.stdin.readline())

for elem in elems:
    counter = 0
    highest_counter = 0
    for i in elem.split():
        if int(i) == 0:
            counter += 1
        elif int(i) == 1:
            highest_counter = max(counter, highest_counter)
            counter = 0
    highest_counter = max(counter, highest_counter)
    print(highest_counter)

# solved
