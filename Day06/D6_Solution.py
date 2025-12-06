# Direct approach for Part 1
# read file
with open("input.txt", "r") as file:
    lines = [[p for p in line.rstrip().split()] for line in file]

print(lines)
total_res = 0
works_count = len(lines[0])
lines_count = len(lines) - 1
for i in range(works_count):
    operator = lines[lines_count][i]
    if operator == '+':
        res = 0
    else:
        res = 1
    for j in range(lines_count):
        if operator == '+':
            res += int(lines[j][i])
        else:
            res *= int(lines[j][i])
    total_res += res

print(f'Part 1:{total_res}')