import sys

num_cases = sys.stdin.readline()
cases = []

for i in range(int(num_cases)):
    cases.append(sys.stdin.readline())

for case in cases:
    distances = case.split()
    a = distances[0]
    distances.sort()
    counter = 0
    for i in distances:
        if int(a) < int(i):
            counter += 1
    print(counter)
