import sys

num_cases = sys.stdin.readline()
cases = []

for i in range(int(num_cases)):
    cases.append(sys.stdin.readline())

for case in cases:
    case_list = case.split()
    if int(case_list[0]) + int(case_list[1]) == int(case_list[2]):
        print("+")
    elif int(case_list[0]) - int(case_list[1]) == int(case_list[2]):
        print("-")
