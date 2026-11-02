import sys

num_lines = int(sys.stdin.readline())
problem_view = []
solved_problems = 0

for i in range(num_lines):
    problem_view.append(sys.stdin.readline().strip("\n"))

for x in problem_view:
    x_list = x.split(" ")
    x_sum = 0
    for x in x_list:
        x_sum += int(x)
    if x_sum >= 2:
        solved_problems += 1

print(solved_problems)

# solved
