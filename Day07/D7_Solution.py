# TODO: can the solution be simplified?
# read file
with open("input.txt", "r") as file:
    diagram = [[l for l in line.rstrip()] for line in file]
rows = len(diagram)
cols = len(diagram[0])
tachyons_split_counter = 0
# Part 1
tachyons_traces = set()
prev_traces = set()
prev_tachyons_traces = set()
obstacles_positions = set()

# Part 2
tachyons_paths = {}
prev_paths = {}
prev_tachyons_paths = {}

for r in range(0, rows + 2, 2):
    # Part 1
    prev_traces = prev_tachyons_traces.copy()
    prev_tachyons_traces = tachyons_traces.copy().union(prev_traces.difference(obstacles_positions))
    tachyons_traces.clear()
    # Part 2
    prev_paths = prev_tachyons_paths.copy()
    carried = {c: w for c, w in prev_paths.items() if c not in obstacles_positions}
    # paths from the prev level
    new_prev = dict(tachyons_paths)
    # plus new ways
    for c, w in carried.items():
        new_prev[c] = new_prev.get(c, 0) + w
    prev_tachyons_paths = new_prev
    tachyons_paths = {}
    # Next step
    obstacles_positions.clear()
    # calc last string and break
    if r == rows:
        break
    for c in range(0, cols):
        if diagram[r][c] == 'S':
            tachyons_traces.add(c)
            tachyons_paths[c] = tachyons_paths.get(c, 0) + 1
        if diagram[r][c] == '^':
            obstacles_positions.add(c)
            if c in prev_tachyons_traces:
                tachyons_traces.add(c-1)
                tachyons_traces.add(c+1)
                tachyons_split_counter += 1
            # calc possible ways
            ways = prev_tachyons_paths.get(c, 0)
            if ways:
                if c - 1 >= 0:
                    tachyons_paths[c - 1] = tachyons_paths.get(c - 1, 0) + ways
                if c + 1 < cols:
                    tachyons_paths[c + 1] = tachyons_paths.get(c + 1, 0) + ways
print(f'Part 1:{tachyons_split_counter}')
print(f'Part 2:{sum(prev_tachyons_paths.values())}')



