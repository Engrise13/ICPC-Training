import sys

case_num = int(sys.stdin.readline())
lengths = []
strings = []

for i in range(case_num):
    lengths.append(int(sys.stdin.readline()))
    strings.append(sys.stdin.readline())

for string in strings:
    counter = 0
    all = list(string)
    all.remove("\n")
    unique = set(all)
    for i in unique:
        counter += 2
        all.remove(i)
    for i in all:
        counter += 1
    print(counter)

# solved
