import sys
from collections import Counter

case_num = sys.stdin.readline()  # case num
results = []


def solve():
    for i in range(int(case_num)):
        sys.stdin.readline()  # length not needed
        case_list = sys.stdin.readline().split()  # makes ["3", "5", "7"] from 3 5 7
        stuff = 0
        values = Counter(case_list)  # counts every occurrence
        for key, value in values.items():
            if value >= 3:
                results.append(str(key))
                stuff += 1
                break
        if stuff == 0:
            results.append("-1")

    print("\n".join(results))


if __name__ == "__main__":
    solve()

# solved
