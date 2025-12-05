def count_unique_in_ranges(ranges):
    # ranges inclusive
    ranges = [(min(l, r), max(l, r)) for l, r in ranges]
    # sort by l, then r
    # to correctly unite overlapping ranges
    ranges.sort()

    total = 0
    cur_l, cur_r = ranges[0]

    for l, r in ranges[1:]:
        # overlap or touch
        if l <= cur_r + 1:
            cur_r = max(cur_r, r)
        else:
            total += cur_r - cur_l + 1
            cur_l, cur_r = l, r

    total += cur_r - cur_l + 1
    return total

# read file
with open("input.txt", "r") as file:
    grid = [line.rstrip() for line in file]

split = grid.index('')
ranges = [(int(g[:g.find('-')]), int(g[g.find('-') + 1:])) for g in grid[0:split]]
fresh_count = 0
for j in range(split + 1, len(grid)):
    for g in ranges:
        start, end = g[0], g[1]
        if start <= int(grid[j]) <= end:
            fresh_count += 1
            break
# for part 2 impossible to combine ids in set of unique nums
# need to be smarter and combine overlapping or touching ranges 
# and count the len of range (end - start + 1)
unique_ids = count_unique_in_ranges(ranges)

print(f"Part 1: {fresh_count}")
print(f"Part 2: {unique_ids}")