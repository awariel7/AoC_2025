# read file
with open("input.txt", "r") as file:
    map = [[l for l in line.rstrip()] for line in file]
# horrible slow solution
movable_rolls = 0
rows_count = len(map)
cols_count = len(map[0])
removed_rolls_pos = []
removing_rounds = dict()
remove_pos = []
round = 0
while 1 == 1:
    round += 1
    movable_rolls = 0
    remove_pos.clear()
    for row in range(rows_count):
        for col in range(cols_count):
            surrounding_rolls_count = 0
            if map[row][col] == '@' and [row, col] not in removed_rolls_pos:
                if row - 1 >= 0:
                    if col - 1 >= 0 and map[row - 1][col - 1] == '@' and [row - 1, col - 1] not in removed_rolls_pos:
                        surrounding_rolls_count += 1
                    if map[row - 1][col] == '@' and [row - 1, col] not in removed_rolls_pos:
                        surrounding_rolls_count += 1
                    if col + 1 < cols_count and map[row - 1][col + 1] == '@' and [row - 1, col + 1] not in removed_rolls_pos:
                        surrounding_rolls_count += 1
                if row + 1 < rows_count:
                    if col - 1 >= 0 and map[row + 1][col - 1] == '@' and [row + 1, col - 1] not in removed_rolls_pos:
                        surrounding_rolls_count += 1
                    if map[row + 1][col] == '@' and [row + 1, col] not in removed_rolls_pos:
                        surrounding_rolls_count += 1
                    if col + 1 < cols_count and map[row + 1][col + 1] == '@' and [row + 1, col + 1] not in removed_rolls_pos:
                        surrounding_rolls_count += 1
                # current row
                if col - 1 >= 0 and map[row][col - 1] == '@' and [row, col - 1] not in removed_rolls_pos:
                    surrounding_rolls_count += 1
                if col + 1 < cols_count and map[row][col + 1] == '@' and [row, col + 1] not in removed_rolls_pos:
                    surrounding_rolls_count += 1
                if surrounding_rolls_count < 4:
                    movable_rolls += 1
                    remove_pos.append([row, col])

    removed_rolls_pos += remove_pos
    removing_rounds[round] = movable_rolls
    if movable_rolls == 0:
        break

print(f'Part 1: {removing_rounds.get(1)}')
print(f'Part 2: {sum(removing_rounds.values())}')

