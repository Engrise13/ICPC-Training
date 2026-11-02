import sys

num_lines = int(sys.stdin.readline())
words = []
final_words = []

for i in range(num_lines):
    words.append(sys.stdin.readline().strip("\n"))

for x in words:
    if len(x) > 10:
        construct_x = ""
        construct_x += x[0]
        construct_x += str(len(x) - 2)
        construct_x += x[-1]
        final_words.append(construct_x)
    else:
        final_words.append(x)

for x in final_words:
    print(x)

# solved
