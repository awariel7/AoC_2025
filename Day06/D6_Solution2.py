def do_normal_math(lines, lines_cnt, last_pos, operator):
    if operator == '+':
        res = 0
    else:
        res = 1
    for n in range(lines_cnt - 1):
        num = ''
        for k in range(last_pos, i):
            num += lines[n][k]
        if operator == '+':
            res += int(num.strip())
        else:
            res *= int(num.strip())
    return res

def do_cephalopod_math(lines, lines_cnt, last_pos, operator):
    if operator == '+':
        res = 0
    else:
        res = 1
    for k in range(i - 1, last_pos - 1, -1):
        num = ''
        for n in range(lines_cnt - 1):
            num += lines[n][k]
        if operator == '+':
            res += int(num.strip())
        else:
            res *= int(num.strip())
    return res

# read file
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]

line_len = len(max(lines, key=len)) + 1
lines_cnt = len(lines)

# modify input to avoid out of range problem
for l_index in range(lines_cnt):
    if len(lines[l_index]) < line_len:
        lines[l_index] += ' ' * (line_len - len(lines[l_index]))

last_pos = 0
total_res_1 = 0
total_res_2 = 0
for i in range(line_len):
    space_cnt = 0
    # search for first space
    if lines[0][i].isdigit():
        space_cnt = 0
        continue
    else:
        space_cnt += 1
        # check whether whole column consists of spaces
        for j in range(1, lines_cnt):
            if lines[j][i].isdigit():
                space_cnt = 0
                break
            else:
                space_cnt += 1
        # if it's a column of spaces
        if space_cnt == lines_cnt:
            operator = lines[lines_cnt-1][last_pos]
            # calc for part 1 (normal math)
            total_res_1 += do_normal_math(lines, lines_cnt, last_pos, operator)
            # calc for part 1 (cephalopod math)
            total_res_2 += do_cephalopod_math(lines, lines_cnt, last_pos, operator)
            last_pos = i + 1


print(f'Part 1:{total_res_1}')
print(f'Part 2:{total_res_2}')


