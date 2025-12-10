# TODO: check the algorythm, understand method

def cross(a, b, p):
    # vector product
    return (b[0] - a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])

def point_on_segment(p, a, b, eps=1e-9):
    # simple check
    # 1) collinear (target point is on the edge of polygon)
    if abs(cross(a, b, p)) > eps:
        return False
    # 2) target point is IN the potential figure
    return (min(a[0], b[0]) - eps <= p[0] <= max(a[0], b[0]) + eps and
            min(a[1], b[1]) - eps <= p[1] <= max(a[1], b[1]) + eps)

def point_in_polygon(p, poly):
    """
    Ray casting algorythm
    """
    n = len(poly)

    # border check
    for i in range(n):
        a = poly[i]
        b = poly[(i + 1) % n]
        if point_on_segment(p, a, b):
            return True

    x, y = p
    inside = False

    for i in range(n):
        x1, y1 = poly[i]
        x2, y2 = poly[(i + 1) % n]

        # trying to check the ray, how many times it crosses the border
        if (y1 > y) != (y2 > y):
            x_int = x1 + (x2 - x1) * (y - y1) / (y2 - y1)
            if x_int > x:
                inside = not inside

    return inside

def rect_corners(p1, p2):
    # get all corners of rectangle
    x1, y1 = p1
    x2, y2 = p2
    left, right = sorted((x1, x2))
    bottom, top = sorted((y1, y2))
    return [(left, bottom), (right, bottom), (right, top), (left, top)]

def rectangle_fits_by_corners(p1, p2, poly):
    corners = rect_corners(p1, p2)
    return all(point_in_polygon(c, poly) for c in corners)

# read file
with open("input.txt", "r") as file:
    lines = [line.rstrip() for line in file]

D = len(lines)
polygon = []
for l in lines:
    x, y = l.split(',')
    polygon.append((int(x), int(y)))

MAX_SQUARE_2 = 0
for i in range(D - 1):
    ix, iy = polygon[i][0], polygon[i][1]
    for j in range(i + 1, D):
        jx, jy = polygon[j][0], polygon[j][1]
        r1 = (ix, iy), (jx, jy)
        if rectangle_fits_by_corners(*r1, polygon):
            sq = (abs(jx - ix) + 1) * (abs(jy - iy) + 1)
            if sq > MAX_SQUARE_2: MAX_SQUARE_2 = sq
#4 599 890 450
#4599890450 ??
print(MAX_SQUARE_2)
