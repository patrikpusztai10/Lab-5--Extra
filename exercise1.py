import matplotlib.pyplot as plt
def cross_product(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0]);


def andrew_graham_scan(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1] #We concatenate the lowe and upper hull
if __name__ == "__main__":
    points = [(30, 60), (15, 25), (0, 30), (70, 30), (50, 40), (50, 10), (20,0),(55, 20)]
    hull = andrew_graham_scan(points)
    x_points, y_points = zip(*points)
    hull_x, hull_y = zip(*hull + [hull[0]])
    plt.figure(figsize=(8, 6))
    plt.scatter(x_points, y_points, color='blue', label='Points')
    plt.plot(hull_x, hull_y, color='red', linestyle='-', marker='o', label='Convex Hull')
    plt.title("Convex Hull Visualization for exercise 1")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.legend()
    plt.grid(True)
    plt.show()
