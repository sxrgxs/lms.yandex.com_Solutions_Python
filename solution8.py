xs, ys, xf, yf = map(int, input().split())

if (xs, ys) != (xf, yf) and ((xs == xf and abs(xs) >= max(abs(ys), abs(yf))) or (ys == yf and abs(ys) >= max(abs(xs), abs(xf)))):
    print("oo")
else:
    max_n = max(abs(xs), abs(ys), abs(xf), abs(yf))
    dx, dy = xf - xs, yf - ys
    points = set()

    for n in range(max_n + 1):
        lines = []
        if n == 0:
            lines = [(0, 'x'), (0, 'y')]
        else:
            lines = [(n, 'x'), (-n, 'x'), (n, 'y'), (-n, 'y')]

        for val, axis in lines:
            if axis == 'x' and dx != 0:
                t = (val - xs) / dx
                if 0 <= t <= 1:
                    yt = ys + t * dy
                    if abs(yt) <= n + 1e-9:
                        points.add((round(val, 8), round(yt, 8)))
            elif axis == 'y' and dy != 0:
                t = (val - ys) / dy
                if 0 <= t <= 1:
                    xt = xs + t * dx
                    if abs(xt) <= n + 1e-9:
                        points.add((round(xt, 8), round(val, 8)))

    if dx == 0 and dy == 0:
        points.add((float(xs), float(ys)))

    print(len(points))