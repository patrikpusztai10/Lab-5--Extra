import math
import matplotlib.pyplot as plt
# Points from the problem
A = (3, -3)
B = (3, 3)
C = (-3, -3)
D = (-3, 3)

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1

def distance(p, q):
    return (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2

def graham_scan(points):
    start = min(points, key=lambda p: (p[1], p[0]))
    points.remove(start)
    points.sort(key=lambda p: (math.atan2(p[1] - start[1], p[0] - start[0]), -distance(start, p)))
    hull = [start]
    for point in points:
        while len(hull) > 1 and orientation(hull[-2], hull[-1], point) != -1:
            hull.pop()
        hull.append(point)

    return hull
#We ask for input for lam and compute the convex hull based on the given input
lam = float(input("Enter a value for lam: "))
M = (-2 + lam, 3 - lam)
points = [A, B, C, D, M]
print("Input Points:", points)
hull = graham_scan(points)
nr_of_points_on_the_border=len(hull)
if lam==0 or lam==5:
#We have observed in Geogebra that when lambda has these values
# the point M is exactly on the border of the convex hull
    nr_of_points_on_the_border+=1
print("Number of points on the border of the convex hull:",nr_of_points_on_the_border)
hull_x, hull_y = zip(*hull + [hull[0]])
plt.figure(figsize=(8, 6))
x_points, y_points = zip(*points)
plt.scatter(x_points, y_points, color='blue', label='Points')
plt.plot(hull_x, hull_y, color='red', linestyle='-', marker='o', label='Convex Hull')
plt.title("Convex Hull Visualization for exercise 2")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid(True)
plt.show()