
from geom2d import *

#a = Point(0,0)
#b = Point(3,4)
#print(a.distance(b))
#print (a==b)
#print (a == Point(0,0))

l1 = [Point(3, 1), Point(0, 0), Point (1, 2)]


l2 = sorted(l1, key= lambda p: p.distance(Point(0,0)))
print(l1)
print(l2)
