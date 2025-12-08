# TODO: unite 2 parts in a single algorythm
# TODO: check for extra memory use or extra variables

# read file
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]
# top N smallest distances
N = 1000
# name all the coordinates for easier work
boxes = dict()
c = 0
for l in lines:
    boxes[c] = [int(n) for n in l.split(',')]
    c += 1

boxes_count = len(boxes)
boxes_distance = dict()
# calc all distances
for i in range(boxes_count - 1):
    i_c = boxes.get(i)
    next_box = i + 1
    if next_box < boxes_count:
        for j in range(next_box, boxes_count):
            k = str(i) + '-' + str(j)
            j_c = boxes.get(j)
            distance = ((j_c[0] - i_c[0])**2 + (j_c[1] - i_c[1])**2 + (j_c[2] - i_c[2])**2)**0.5
            boxes_distance[k] = distance

# sort by distance, slice top N
sorted_boxes_distance = dict(
    sorted(boxes_distance.items(), key=lambda item: item[1])[:N]
)

# build graph from top N smallest edges
adj = dict()
for key in sorted_boxes_distance.keys():
    a_str, b_str = key.split("-")
    a, b = int(a_str), int(b_str)
    adj.setdefault(a, set()).add(b)
    adj.setdefault(b, set()).add(a)

# get clusters
# set of visited nodes
visited = set()
# clusters
components = []
for node in adj.keys():
    # if node was visited - skip
    if node in visited:
        continue
    # starting cluster
    stack = [node]
    visited.add(node)
    comp = []

    while stack:
        x = stack.pop()
        comp.append(x)

        for y in adj[x]:
            if y not in visited:
                visited.add(y)
                stack.append(y)
    components.append(sorted(comp))
# calc res
res = 1
sorted_components = sorted([len(c) for c in components], reverse=True)
for n in range(3):
    res *= sorted_components[n]
print(f'Part 1: {res}')

# recreate distance dictionary
# get full dict
sorted_boxes_distance_full = dict(
    sorted(boxes_distance.items(), key=lambda item: item[1])
)
res2 = 1
# set for checking
must_be_visited = set(i for i in range(len(lines)))
# set of visited nodes
visited = set()
empty_set = set()
for k in sorted_boxes_distance_full.keys():
    a_str, b_str = k.split("-")
    if a_str not in visited:
        visited.add(int(a_str))
    if b_str not in visited:
        visited.add(int(b_str))
    # if we visited all nodes, this means that the last edge was connecting
    # product of x coordinates will be the answer
    if must_be_visited.difference(visited) == empty_set:
        x1 = boxes.get(int(a_str))[0]
        x2 = boxes.get(int(b_str))[0]
        res2 = x1 * x2
        break
print(f'Part 2: {res2}')




