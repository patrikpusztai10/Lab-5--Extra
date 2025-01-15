import matplotlib.pyplot as plt
def cross_product(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1])-(a[1]-o[1])*(b[0]-o[0]);

def jarvis_march(points):
    n = len(points)
    if n < 3:
        return points
    i=1
    hull = []
    leftmost = min(points, key=lambda p: p[0])
    point_on_hull = leftmost
    while True:
        hull.append(point_on_hull)
        next_point = points[0]
        for p in points:
            if next_point == point_on_hull or cross_product(point_on_hull, next_point, p) < 0:
                next_point = p
        point_on_hull = next_point

        if point_on_hull == leftmost:
            break
        print("The hull consists of the points:"+str(hull))
        i+=1
    print("The hull consists of the points:" + str(hull))
    return hull
points = [(1, 10), (-2, 7), (3, 8), (4, 10), (5, 7), (6, 7), (7, 11)]
hull = jarvis_march(points)
hull_x, hull_y = zip(*hull + [hull[0]])
plt.figure(figsize=(8, 6))
x_points, y_points = zip(*points)
plt.scatter(x_points, y_points, color='blue', label='Points')
plt.plot(hull_x, hull_y, color='red', linestyle='-', marker='o', label='Convex Hull')
plt.title("Convex Hull Visualization for exercise 3")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()
#In this case the lower part of the convex hull consists of the points
#(-2,7) , (5,7) and (6,7) which are all collinear