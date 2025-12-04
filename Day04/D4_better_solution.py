# read file
with open("input.txt", "r") as file:
    grid = [list(line.rstrip()) for line in file]

rows_count = len(grid)
cols_count = len(grid[0])

removing_rounds = {}
round_num = 0

# list of all 8 directions
directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),          (0, 1),
    (1, -1),  (1, 0), (1, 1),
]

while True:
    round_num += 1
    remove_pos = []

    for row in range(rows_count):
        for col in range(cols_count):
            if grid[row][col] != '@':
                continue
            surrounding = 0
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows_count and 0 <= nc < cols_count:
                    if grid[nr][nc] == '@':
                        surrounding += 1

            if surrounding < 4:
                remove_pos.append((row, col))

    movable_rolls = len(remove_pos)
    removing_rounds[round_num] = movable_rolls

    if movable_rolls == 0:
        break

    # delete removed rolls from map
    for row, col in remove_pos:
        grid[row][col] = '.'

print(f"Part 1: {removing_rounds.get(1, 0)}")
print(f"Part 2: {sum(removing_rounds.values())}")