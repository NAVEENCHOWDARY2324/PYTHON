
import math

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
r = int(input())

d = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
if (d==r):
    print(d)
    print("point is on the circle")
elif (d<r):
    print(d)
    print("point is inside the circle")
else:
    print(d)
    print("point is outside the circle")
