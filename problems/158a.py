import sys

data = sys.stdin.readline()
contestants = sys.stdin.readline()

n = int(data.split()[0])
k = int(data.split()[1])

contestants_list = contestants.split()
int_contestants_list = []
passed = []

for x in contestants_list:
    if int(x) > 0:
        int_contestants_list.append(int(x))

for x in int_contestants_list:
    if x >= int_contestants_list[k - 1]:
        passed.append(x)

print(len(passed))

# test 7: runtime error
