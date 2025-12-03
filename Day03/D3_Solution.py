def max_num(k, digits_list, start_idx, res):
    n = len(digits_list)
    if len(res) == k:
        return res
    remaining = k - len(res)
    last_start = n
    digits_sublist = digits_list[start_idx : last_start - remaining + 1]
    max_digit = max(digits_sublist)
    # global position in main list
    s_pos = start_idx + digits_sublist.index(max_digit)
    return max_num(k, digits_list, s_pos + 1, res + max_digit)


# read file
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]
total_sum_1 = 0
total_sum_2 = 0
for l in lines:
    start_idx = 0
    res = ""
    digits_list = [s for s in l]
    max_joltage = max_num(2, digits_list, 0, res)
    print(max_joltage)
    total_sum_1 += int(max_joltage)
    max_joltage_2 = max_num(12, digits_list, 0, res)
    print(max_joltage_2)
    total_sum_2 += int(max_joltage_2)
print(f"Part 1: {total_sum_1}")
print(f"Part 2: {total_sum_2}")
