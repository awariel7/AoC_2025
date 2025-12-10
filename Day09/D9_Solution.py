

# read file
with open("test.txt", "r") as file:
    lines = [line.rstrip() for line in file]

D = len(lines)
polygon = []
for l in lines:
    x, y = l.split(',')
    polygon.append((int(x), int(y)))

MAX_SQUARE = 0
MAX_SQUARE_2 = 0
for i in range(D - 1):
    ix, iy = polygon[i][0], polygon[i][1]
    for j in range(i + 1, D):
        jx, jy = polygon[j][0], polygon[j][1]
        # Part 1
        sq = (abs(jx - ix) + 1) * (abs(jy - iy) + 1)
        if sq > MAX_SQUARE: MAX_SQUARE = sq
        # Part 2
        # Check all points of rectanle whether they are in the polygon
        p1 = (ix, iy)
        p2 = (ix, jy)
        p3 = (jx, jy)
        p4 = (jx, iy)
        if point_in_convex_polygon(p1, polygon)\
            and point_in_convex_polygon(p2, polygon)\
            and point_in_convex_polygon(p3, polygon)\
            and point_in_convex_polygon(p4, polygon):
                if MAX_SQUARE > MAX_SQUARE_2: MAX_SQUARE_2 = MAX_SQUARE

print(f'Part 1: {MAX_SQUARE}')
print(f'Part 2: {MAX_SQUARE_2}')
